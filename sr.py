from urllib2 import urlopen
from json import load
url = "http://api.sr.se/api/v2/playlists/rightnow?channelid=164"
url += "&format=json"
response = urlopen(url)
json_obj = load(response)


def get_song():
	try:
		song = json_obj['playlist']['song']['description']
		print "Song playing now: " + song
		return song

	except:
		'''
		song = 	json_obj['playlist']['nextsong']['description']
		print "Next song is: " + song
		'''
		print "kan inte visa denna song "

def get_previous_song():
	try:
		song = json_obj['playlist']['previoussong']['description']
		print "Previous song: " + song
		return song
	except:
		print "Finns ingen information om previous song"	

get_song()
get_previous_song()



'''
print json_obj : visar hela skiten
print song
'''
