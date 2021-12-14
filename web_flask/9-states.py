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


@app.route('/states')
def statesList():
    """shows the list of all State objects"""
    states = storage.all(State)
    return flask.render_template('9-states.html', states=states, idNum=None)


@app.route('/states/<id>')
def statesID(id):
    """shows the list of all State objects"""
    states = storage.all(State)
    idList = [o.id for o in states.values()]
    sId = "State." + id
    return flask.render_template('9-states.html',
                                 states=states, idNum=id, idList=idList,
                                 sId=sId)


# will run without using flask run. Now can run as a python file
if __name__ == '__main__':
    app.debug = True
    app.run(debug=True, host="0.0.0.0", port=5000)
