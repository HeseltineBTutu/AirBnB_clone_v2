#!/usr/bin/python3

"""
This module defines a simple Flask web application.

The application includes four routes:
1. The root route ('/') displays "Hello HBNB!".
2. The '/hbnb' route displays "HBNB".
3. The '/c/<text>' route displays "C " followed by the value
of the 'text' variable
   (replace underscores '_' with spaces).
4. The '/python/<text>' route displays "Python " followed by
the value of the 'text' variable
   (replace underscores '_' with spaces). The default value
   for 'text' is "is cool".

Usage:
    To start the application, run this script. The application will
    listen on 0.0.0.0 (all available network interfaces) on port 5000.

Routes:
    /: Displays "Hello HBNB!" when visited.
    /hbnb: Displays "HBNB" when visited.
    /c/<text>: Displays "C " followed by the value of
    'text' (replace '_' with space).
    /python/<text>: Displays "Python " followed by the value
    of 'text' (replace '_' with space).

Examples:
    - Visit http://0.0.0.0:5000/ in your browser to see "Hello HBNB!".
    - Visit http://0.0.0.0:5000/hbnb in your browser to see "HBNB".
    - Visit http://0.0.0.0:5000/c/is_fun in your browser to see "C is fun".
    - Visit http://0.0.0.0:5000/python/is_magic in your browser to
    see "Python is magic".
    - Visit http://0.0.0.0:5000/python in your browser to see
    "Python is cool" (default).
    - Visit http://0.0.0.0:5000/python/ in your browser to see
    "Python is cool" (default).

This script can also be used as a template for creating simple
Flask applications.
"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route to display "Hello HBNB!" when visiting the root URL ('/').

    Returns:
        str: A simple greeting message.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route to display "HBNB" when visiting the '/hbnb' URL.

    Returns:
        str: A message displaying "HBNB".
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Route to display "C " followed by the value of the 'text' variable.

    Args:
        text (str): The text provided in the URL.

    Returns:
        str: A message displaying "C " followed by
        'text' (replace '_' with space).
    """
    return "C {}".format(escape(text).replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Route to display "Python " followed by the value of the 'text' variable.

    Args:
        text (str): The text provided in the URL. Defaults to
        'is cool' if not provided.

    Returns:
        str: A message displaying "Python " followed by 'text'
        (replace '_' with space).
    """
    return "Python {}".format(escape(text).replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
