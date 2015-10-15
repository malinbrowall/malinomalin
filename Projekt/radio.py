
# -*- coding: utf-8 -*-

from bottle import *
import json
import spotipy

@route("/static/<filepath:path>")
def server_static(filepath):
	"""CSS"""
	return static_file(filepath, root="static")

@route('/')
def start():
	'''Mainpage'''
	return template ("index")

run(host='localhost', port=8080, debug=True, reloader=True)