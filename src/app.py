from flask import Flask, render_template

from src.common.database import Database

__author__ = 'nikos'

app = Flask(__name__)
app.config.from_object('src.config')
app.secret_key = "123"


@app.before_first_request
def init_db():
    Database.initialize()


# @app.route('/')
# def hello_world():
#     return "Hello, world!"

# if __name__ == "__main__":
#     app.run(debug=True, port=4990)
# We did like that before using run.py


@app.route('/')
def home():
    return render_template('home.jinja2')


from src.models.users.views import user_blueprint
from src.models.alerts.views import alert_blueprint
from src.models.stores.views import store_blueprint

app.register_blueprint(user_blueprint, url_prefix="/users")
app.register_blueprint(alert_blueprint, url_prefix="/alerts")
app.register_blueprint(store_blueprint, url_prefix="/stores")
