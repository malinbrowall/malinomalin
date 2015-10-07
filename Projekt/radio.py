# coding: utf-8
# Author: Malin Browall och Malin Larsson

from bottle import *



@route("/")
def go():
    """
    Första sidan
    """
    return template("index")




run(host='localhost', port=8080, debug=True, reloader=True)