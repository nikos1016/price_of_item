from flask import Blueprint

__author__ = 'nikosD'


item_blueprint = Blueprint('items', __name__)

@item_blueprint.route('/item/<stirng:name>')
def item_page(name):
    pass


