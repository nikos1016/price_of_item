from src.app import app

__author__ = 'nikos'

app.run(debug=app.config['DEBUG'], port=4990)