#!/usr/bin/python3
"""starts a Flask web application"""
from logging import error
from flask import Flask
import flask
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(context):
    storage.close()


@app.route('/hbnb_filters')
def statesList():
    """inputs cities and states to actual bnb HTML"""
    states = storage.all(State)
    am = storage.all(Amenity)
    return flask.render_template('10-hbnb_filters.html', states=states, am=am)


# will run without using flask run. Now can run as a python file
if __name__ == '__main__':
    app.debug = True
    app.run(debug=True, host="0.0.0.0", port=5000)
