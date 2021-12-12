#!/usr/bin/python3
"""starts a Flask web application"""
from logging import error
from flask import Flask
import flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/', strict_slashes=False)
def hello():
    """displays on index page"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """displays on HBNH page"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cRoute(text):
    """displays on any child of /c"""
    if '_' in text:
        text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python')
@app.route('/python/<text>')
def opPy(text="is cool"):
    """displays on any child of python with optional parameters"""
    if '_' in text:
        text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<n>')
def nummy(n):
    """displays on any child of number if number"""
    try:
        return '{} is a number'.format(int(n))
    except Exception:
        flask.abort(404)


# will run without using flask run. Now can run as a python file
if __name__ == '__main__':
    app.debug = True
    app.run(debug=True, host="0.0.0.0", port=5000)
