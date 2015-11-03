#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sr import *
from spot import *
from urllib2 import urlopen
from json import *
import requests
from bottle import *
import requests 

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
	""" Kör funktionerna get_song och spot_search """
	sr_song, text = get_song()
	print sr_song 
	spoty = spot_search(sr_song)


	if request.headers.get('Accept') == "application/json":
		response.set_header("Content-Type", "application/json")
		json_obj = {"sverigesradio_P3": {"song_artist": sr_song, "spotify_url": spoty}}
		return dumps(json_obj)
	else:
		return template("play", sr_song=sr_song, spoty=spoty, text=text)


@route('/nextsong/')
def next(): 	
	""" Kör funktionerna get_nextsong och spot_search """
	sr_song, text = get_nextsong()
	print sr_song 
	spoty = spot_search(sr_song)

	
	return template("play", sr_song=sr_song, spoty=spoty, text=text)


run(host='localhost', port=8080, debug=True, reloader=True)
main()
