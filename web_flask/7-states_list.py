#!/usr/bin/python3
'''Starts a Flask Web app'''
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def teardown(context):
    """Flask Teardown"""
    storage.close()

@app.route('/states_list', strict_slashes=False)
def statesList():
    States = storage.all(State)
    return render_template("7-states_list.html", States=States)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
