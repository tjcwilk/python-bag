#!/usr/bin/python

#
# Web Scraping
#	Template code for interacting with websites using urlLib
#

import urllib
import urllib2


def basicPull(url):
  req = urllib2.Request( "http://wilkins.io")
  response = urllib2.urlopen(req)
  the_page = response.read()

  print the_page


def postRequestArgs():
	# Parsing the data arguments tells urllub to do a POST

	url = 'http://wilkins.io'
	# wilkins.io dosnt handle this so it wont return anything. use a different url.
	values = {'name' : 'alice',
	          'location' : 'UK',
	          'language' : 'English' }

	data = urllib.urlencode(values)
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	the_page = response.read()

def getRequestArgs():
	# Passing args like this tells urllib to do a GET request
	data = {}
	data['name'] = 'alice'
	data['location'] = 'UK'
	data['language'] = 'English'

	url_values = urllib.urlencode(data)

	url = 'http://wilkins.io' # Wont handle this
	full_url = url + '?' + url_values
	data = urllib2.urlopen(full_url)

def defineHeaders()
	url = 'http://wilkins.io'
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	values = {'name' : 'alice',
	          'location' : 'UK',
	          'language' : 'English' }
	headers = { 'User-Agent' : user_agent }

	data = urllib.urlencode(values)
	req = urllib2.Request(url, data, headers)
	response = urllib2.urlopen(req)
	the_page = response.read()

