#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import unirest

print "Retrieving: new offers"
spreadsheet = "https://spreadsheets.google.com/feeds/list/1VPHB9pRPCbG6icFp2KhXRhOA7wA5I3K6khOoYBW24CQ/od6/public/values?alt=json"

response = unirest.get(spreadsheet)

features = []

for e in response.body["feed"]["entry"]:

	tmp = {
		"geometry" : {
			"x": float(e["gsx$longitud"]["$t"].encode('utf-8')),
			"y": float(e["gsx$latitud"]["$t"].encode('utf-8'))
		},
	    "attributes" : {
	      "img" : e["gsx$imagenopcional"]["$t"].encode('utf-8'),
	      "msg" : e["gsx$texto"]["$t"].encode('utf-8')
	    }
	}
	features.append(tmp)
	
#url = "http://httpbin.org/post"
url = "http://services.arcgis.com/Q6ZFRRvMTlsTTFuP/arcgis/rest/services/BigOffer/FeatureServer/0/addFeatures"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

# Documentacion
# http://resources.arcgis.com/en/help/arcgis-rest-api/index.html#/Add_Features/02r30000010m000000/
data = {
	"features" : features
}

print "Updating: feature service"
r = unirest.post(url, headers={ "Accept": "application/json" }, params=data)

#print json.dumps(r.body)
