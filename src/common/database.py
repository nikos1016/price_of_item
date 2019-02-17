import os

import pymongo

__author__ = 'nikosD'


class Database(object):
    URI = os.environ.get("MONGOLAB_URI") #universal resource identifier
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['PythonWeb']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection, query, data):
        Database.DATABASE[collection].update(query, data, upsert=True) #upsert=True is to insert instead of updating if query is not into the Database

    @staticmethod
    def remove(collection, query):
        Database.DATABASE[collection].remove(query)