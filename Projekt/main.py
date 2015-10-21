#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sr import *
from spot import *
from urllib2 import urlopen
from json import load
import requests
from bottle import *

@route("/static/<filepath:path>")
def style(filepath): 
	""" CSS """
	return static_file(filepath, root="static")

@route("/")
def start(): 
	""" Första sidan """
	return template("index")

@route('/play/')
def main(): 
	""" play """
	song = get_song()
	spoty = spot_search(song)

	'''print song + str(spoty)'''
	return template("play", song=song, spoty=spoty,)



run(host='localhost', port=8080, debug=True, reloader=True)
main()
