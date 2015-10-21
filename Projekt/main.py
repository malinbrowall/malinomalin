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
	sr_song, text = get_song()
	print sr_song 
	spoty = spot_search(sr_song)

	
	return template("play", sr_song=sr_song, spoty=spoty, text=text)



run(host='localhost', port=8080, debug=True, reloader=True)
main()
