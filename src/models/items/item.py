import re
import uuid
import requests
from bs4 import BeautifulSoup
from src.common.database import Database
import src.models.items.constants as ItemContants
from src.models.stores.store import Store

__author__ = 'nikosD'

class Item(object):
    def __init__(self, name, url, price=None, _id=None):
        self.name = name
        self.url = url
        store = Store.find_by_url(url)
        self.tag_name = store.tag_name
        self.query = store.query
        self.price = None if price is None else price
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<Item {} with URL {}>".format(self.name, self.url)

    def load_price(self):
        # Amazon: <span id="priceblock_ourprice" class="a-size-medium a-color-price">$328.00</span>
        request = requests.get(self.url)
        content = request.content
        soup = BeautifulSoup(content, "html.parser")
        element = soup.find(self.tag_name, self.query)
        string_price = element.text.strip()

        pattern = re.compile("(\d+.\d+)") #$115.00
        match = pattern.search(string_price)
        self.price = float(match.group())

        return match.group()

    def save_to_mongo(self):
        # Insert JSON representation
        Database.update(ItemContants.COLLECTION, {'_id': self._id}, self.json())

    def json(self):
        return {
            "_id": self._id,
            "name": self.name,
            "url": self.url,
            "price": self.price
        }

    @classmethod
    def get_by_id(cls, item_id):
        return cls(**Database.find_one(ItemContants.COLLECTION, {"_id": item_id}))