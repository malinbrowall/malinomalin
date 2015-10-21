#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sr import *
from spot import *
from urllib2 import urlopen
from json import load
import requests

def main():
	song = get_song()
	spoty = spot_search(song)
	print song



main()