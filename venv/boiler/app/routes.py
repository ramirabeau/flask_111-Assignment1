#!/usr/bin/env python3
#-*- coding: utf8 -*-
"""Flask routes"""

# From the app module import the app variable
from app import app

# A line prefixed by "@" is a decorator in python
# We are using the route function to map a view function to
# a route

@app.route("/")
def index():  # The view function that the route maps to.
    return "<h1>Hello, World!</h1>"

@app.route("/aboutme")
def aboutme():
    first_name = "Raven"
    last_name = "Mirabeau"
    hobby = "RPi Stack"

#    return{
#        "first_name": "Raven",
#        "last_name": "Mirabeau",
#        "hobby": "I like to experiment with Raspberry Pi Stacks"
#    }