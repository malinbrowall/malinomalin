#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib2 import urlopen
from json import load
url = "http://api.sr.se/api/v2/playlists/rightnow?channelid=164"
url += "&format=json"
response = urlopen(url)
json_obj = load(response)


def get_nextsong():
	try:
		sr_song = 	json_obj['playlist']['nextsong']['description']
		text = "Next song: "
		return (sr_song, text)
	except:
		text = "Is not avaliable right now"
		return text

def get_previoussong():
	try:
		sr_song = json_obj['playlist']['previoussong']['description']
		text = "Previous song: "
		return (sr_song, text)
	except:	
		text = "Is not avaliable right now"
		return text	

def get_songplayingnow():
	try:
		sr_song = json_obj['playlist']['song']['description']
		text = "Song playing now: "
		return (sr_song, text)
	except:
		text = "Is not avaliable right now"
		return text

def get_song():
	'''Forsoker hamta lat och artist som spelas just nu pa SR och returnerar det tillsammans med textstrangen
	Om det inte gar hamtas nasta lat eller lat som spelades tidigare'''
	try:
		sr_song = json_obj['playlist']['song']['description']
		text = "Song playing now: "
		return (sr_song, text)

	except:
		try:
			sr_song = 	json_obj['playlist']['nextsong']['description']
			text = "Next song: "
			return (sr_song, text)

		except:
			sr_song = json_obj['playlist']['previoussong']['description']
			text = "Previous song: "
			return (sr_song, text)
