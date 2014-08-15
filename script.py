# Script for Mopub sample request
# Junyong Suh <jsuh@zynga.com>

import sys
import urllib2
import time

MOPUB_TEST_IDS = {'2a64cacd316649238e1960f3a2579feb','56f3e9dc861a4d1492f7e6f13b619c05','b4aaaf72ff2148979df159a8f4dda9b5','f1958f2b82224a82bdf200b193372bc6','ab0318913ada4416af63e3b9140dee19','e4e514dabbe64507ae53c2fd38c7c607'}

def mopubRequest(mopubAdUnitId):
	# Mopub Sample Request
	url = 'http://ads.mopub.com/m/ad?id=2a64cacd316649238e1960f3a2579feb&v=1&udid=sha:CF95DB7F559BD1FC1ACC842135E2CA536C14F8AE&tp=zynga&mr=1&admin_debug_mode=0&include='+ mopubAdUnitId
	# url = 'http://ads.mopub.com/m/ad?id='+ mopubAdUnitId  +'&v=1&udid=sha:CF95DB7F559BD1FC1ACC842135E2CA536C14F8AE&tp=zynga&mr=1'
	# url = 'http://ads.mopub.com/m/ad?mr=1&v=1&udid=sha:B6E38584B64C04F621B21EF1763A3118AA28B4BA&q=key:value&id='+ mopubAdUnitId
	print "\n[Request] \n"+ url

	# send a request and get response
	response = urllib2.urlopen(url, timeout=2).read()

	# Try 10 times with 2 secs cooldown time if HTTP Status is not 200 or empty response
	retryCount = 1
	retryUntil = 10
	while (not response or "<html>" not in response)  and retryCount < retryUntil:
		if ("HTTP Status" in response):
		 	print 'HTTP Status is not 200 from the server (trying '+ str(retryCount) +'/'+ str(retryUntil) +')'
		elif (not response):
			print 'No response (trying '+ str(retryCount) +'/'+ str(retryUntil) +')'
		elif ("<html>" not in response):
			print response +' (trying '+ str(retryCount) +'/'+ str(retryUntil) +')'
		retryCount = retryCount + 1
		time.sleep(2)
		response = urllib2.urlopen(url).read()

	return response

########################################################################
#
# Main function
#
########################################################################
for mopubAdUnitId in MOPUB_TEST_IDS:
	result = mopubRequest(mopubAdUnitId)
	if (not result):
		print '[Response]\nNo valid response for Ad Unit ID: '+ mopubAdUnitId + '\n'
	else:
		print '[Response]\n' + result + '\n'

# All Good!
exit(0)
