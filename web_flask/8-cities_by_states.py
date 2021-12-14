#!/usr/bin/python3
"""starts a Flask web application"""
from logging import error
from flask import Flask
import flask
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(context):
    storage.close()


@app.route('/cities_by_states')
def statesList():
    """shows the list of all State objects"""
    states = storage.all(State)
    return flask.render_template('8-cities_by_states.html', states=states)


# will run without using flask run. Now can run as a python file
if __name__ == '__main__':
    app.debug = True
    app.run(debug=True, host="0.0.0.0", port=5000)
