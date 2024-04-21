#!/usr/bin/python3

"""
This module defines a simple Flask web application.

The application includes a single route to display "Hello HBNB!"
when visiting the root URL ('/').

Usage:
    To start the application, run this script. The application will
    listen on 0.0.0.0 (all available network interfaces) on port 5000.

Routes:
    /: Displays "Hello HBNB!" when visited.

Example:
    Visit http://0.0.0.0:5000/ in your browser to see the message.

This script can also be used as a template for creating simple
Flask applications.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route to display "Hello HBNB!" when visiting the root URL.

    Returns:
        str: A simple greeting message.
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
