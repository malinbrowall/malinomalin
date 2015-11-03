#!/usr/bin/env python
# -*- coding: utf-8 -*-

import spotipy
def spot_search(sr_song):
	''' med resultat fran sr gors en sokfraga pa spotify och returnerar en url med forsta matchande lat pa Spotify'''	
	sp = spotipy.Spotify()
	results = sp.search(q=sr_song, limit=1)
	for item in results['tracks']['items']:
		return item['external_urls']['spotify']
		
	