#!/usr/bin/python3
"""task 4
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ display greeting
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """ display hbnb
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def what_is_c(text):
    """ display what is c
    """
    return 'C %s' % text


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def what_is_python(text="is cool"):
    """ display what is python
    """
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def to_n_or_not_to_n(n):
    """ display if n is integer
    """
    return '%d is a number' % n

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
