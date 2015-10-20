#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sr import *
import spotipy
sp = spotipy.Spotify()
artisten = get_song()
results = sp.search(q=artisten, limit=1)
'''print results'''
for item in results['tracks']['items']:
	print item['name']
