from sys import argv
import hashlib
from random import random
import urllib2

script, adunitid = argv

def mp_udid(raw_udid):
	m = hashlib.sha1()
	m.update(raw_udid)
	hashed_udid = m.hexdigest().upper()
	return 'sha:'+hashed_udid

def warmup(adunitid):
	count=0
	response=''
	for i in range(3000):
		url='http://ads.mopub.com/m/ad?id='+adunitid+'&ua=Mozilla/5.0%20%28iPhone%3B%20U%3B%20CPU%20iPhone%20OS%204_0%20like%20Mac%20OS%20X%3B%20en-US%29%20AppleWebKit/532.9%20%28KHTML%2C%20like%20Gecko%29%20Version/4.0.5%20Mobile/8A293%20Safari/6531.22.7&ip=204.28.127.10&q=&udid='+mp_udid(str(random()))+'&exclude=&country=US&ll=40.742536,-73.9848984'
		print url
		response= urllib2.urlopen(url).read()
		print response
		count+=1
		if response=='':
			print 'ad unit tested '+str(count)+' times'
		else:
			print response
			print 'ad unit tested '+str(count)+' times'

# Main
warmup(adunitid)
