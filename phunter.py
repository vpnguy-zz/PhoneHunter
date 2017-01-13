#psearch.py

import urllib2
import base64
import json
import sys

#Insert these keys from your Twilio dashboard
account_sid = "Account SID here"
auth_token = "Account auth_token"
targetnum = sys.argv[1]

baseurl = "https://lookups.twilio.com/v1/PhoneNumbers/%s?Type=carrier&Type=caller-name&AddOns=nextcaller_advanced_caller_id" %  (targetnum)


req = urllib2.Request(baseurl)
base64string = base64.b64encode('%s:%s' % (account_sid,auth_token))
req.add_header("Authorization", "Basic %s" % base64string)   
response = urllib2.urlopen(req)
page = response.read()
jsonarray = json.loads(page)
jshort = json.dumps(jsonarray['add_ons']['results']['nextcaller_advanced_caller_id']['result']['records'][0])
jshort = json.loads(jshort)


#Dump some data, full listing of possible output via "print jshort" or https://www.twilio.com/marketplace/add-ons/nextcaller-advanced-caller-id
print "Name: " + jsonarray['add_ons']['results']['nextcaller_advanced_caller_id']['result']['records'][0]['name']
print "Address Line1: " + jshort['address'][0]['line1']
print "Address Line2: " + jshort['address'][0]['line2']
print "City: " + jshort['address'][0]['city']
print "State: " + jshort['address'][0]['state']
print "Zip: " + jshort['address'][0]['zip_code']
print "Email: " +jshort['email']
