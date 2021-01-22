#!/usr/bin/env python3
# -*- coding utf8 -*-
"""HTTP route definitions"""

from app import app

@app.route("/")
def index():
    return "<h1>Hello World!  =)</h1>"

@app.route("/aboutme")
def aboutme():
    my_dictionary = dict()
    my_dictionary["first_name"] = "Raven"
    my_dictionary["last_name"] = "Mirabeau"
    my_dictionary["hobbies"] = "RPI Projects"
    
    return my_dictionary

@app.route("/aboutme2")
def aboutme_html():
    first_name = "Raven"
    last_name = "Mirabeau"
    hobbies = "RPI Projects"
    about_me = """<h1>First name: %s;<br>
                Last name: %s;<br>
                Hobbies: %s</h1>""" %(
                    first_name, 
                    last_name, 
                    hobbies)

    return about_me
    
    