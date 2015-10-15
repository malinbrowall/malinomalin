from urllib2 import urlopen
from json import *



url = "http://api.sr.se/api/v2/playlists/rightnow?channelid=164&format=json"
response = urlopen(url)
json_obj = load(response)
#'playlist' -> 'song' -> 'description'
try:
	json_prev = json_obj['playlist']['previoussong']['description']
	json_song = json_obj['playlist']['song']['description']
	json_next = json_obj['playlist']['nextsong']['description']
	print "Previoussong : " + json_prev + " Playing now : " + json_song + " Next song " + json_next

	#'playlist' -> 'song' -> 'description'  
except KeyError:
	json_song = json_obj['playlist']['song']['description']
	print "Playing now : " + json_song

	try:
		json_next = json_obj['playlist']['nextsong']['description']
		print "Nextsong : " + json_next

	except KeyError:
		json_prev = json_obj['playlist']['previoussong']['description']
		print "Previoussong : " + json_prev