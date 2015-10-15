from urllib2 import urlopen
from json import load

url = "http://api.sr.se/api/v2/playlists/rightnow?channelid=164"
url += "&format=json"

response = urlopen(url)
json_obj = load(response)

def get_song():
	#'playlist' -> 'song' -> 'description' + 'playlist' -> 'nextsong' -> 'description' 
	# försöker att hämta och printa låt som spelas just nu och nästkommande låt
	try:
		json_song = json_obj['playlist']['song']['description']
		json_next = json_obj['playlist']['nextsong']['description']
		print " Playing now : " + json_song + "\n" + " Next song: " + json_next
		return json_song("desctiption") + json_next("description")

	#'playlist' -> 'nextsong' -> 'description'  
	# om ingen låt spelas så blir det ett KeyError och då printas bara nästkommande låt
	except KeyError:
		json_next = json_obj['playlist']['nextsong']['description']
		print "Next song: " + json_next
		return json_song("desctiption") 

def get_previous_song():
	# försöker att hämta och printa låt som spelades nyss
	try:
		json_prev = json_obj['playlist']['previoussong']['description']
		print "Previous song: " + json_prev
		return json_prev("desctiption") 
	# om ingen information finns om den låten (vilket det sällan finns) så printas texten nedan
	except:
		print "Finns ingen information om previous song"	

get_song()
get_previous_song()



