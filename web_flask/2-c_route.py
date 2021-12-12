#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask
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
        newText = text.replace('_', ' ')
    return 'c {}'.format(newText)


# will run without using flask run. Now can run as a python file
if __name__ == '__main__':
    app.debug = True
    app.run(debug=True, host="0.0.0.0", port=5000)
