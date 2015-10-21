#!/usr/bin/env python
# -*- coding: utf-8 -*-

import spotipy
def spot_search(sr_song):
	sp = spotipy.Spotify()
	results = sp.search(q=sr_song, limit=1)
	for item in results['tracks']['items']:
		return item['external_urls']['spotify']
		
	