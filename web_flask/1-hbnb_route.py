#!/usr/bin/python3

"""
This module defines a simple Flask web application.

The application includes two routes:
1. The root route ('/') displays "Hello HBNB!".
2. The '/hbnb' route displays "HBNB".

Usage:
    To start the application, run this script. The application will
    listen on 0.0.0.0 (all available network interfaces) on port 5000.

Routes:
    /: Displays "Hello HBNB!" when visited.
    /hbnb: Displays "HBNB" when visited.

Examples:
    - Visit http://0.0.0.0:5000/ in your browser to see "Hello HBNB!".
    - Visit http://0.0.0.0:5000/hbnb in your browser to see "HBNB".

This script can also be used as a template for creating
simple Flask applications.
"""

from flask import Flask

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
