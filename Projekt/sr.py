from urllib2 import urlopen
from json import *



url = "http://api.sr.se/api/v2/playlists/rightnow?channelid=164&format=json"
response = urlopen(url)
json_obj = load(response)
#'playlist' -> 'song' -> 'description'
try:
	json_song = json_obj['playlist']['song']['description']
	json_next = json_obj['playlist']['nextsong']['description']
	print " Playing now : " + json_song + "\n" + " Next song: " + json_next

	#'playlist' -> 'nextsong' -> 'description'  
except KeyError:
	json_song = json_obj['playlist']['nextsong']['description']
	print "Next song: " + json_song