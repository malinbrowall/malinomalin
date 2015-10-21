from urllib2 import urlopen
from json import load
url = "http://api.sr.se/api/v2/playlists/rightnow?channelid=164"
url += "&format=json"
response = urlopen(url)
json_obj = load(response)


def get_song():
	try:
		song = json_obj['playlist']['song']['description']
		return "Song playing now: " + song

	except:
		try:
			song = 	json_obj['playlist']['nextsong']['description']
			return "Next song is: " + song

		except:
			song = json_obj['playlist']['previoussong']['description']
			return "Previous song: " + song






'''
print json_obj : visar hela skiten
print song
'''
