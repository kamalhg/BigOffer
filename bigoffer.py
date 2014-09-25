import arcpy
import arcrest
import json
import requests

spreadsheet = "https://spreadsheets.google.com/feeds/list/1VPHB9pRPCbG6icFp2KhXRhOA7wA5I3K6khOoYBW24CQ/od6/public/values?alt=json"

response = requests.get(spreadsheet)
json_data = json.loads(response.text)



try:
    fc = r"<some feature class>"
    url = "<service URL>"
    username = "<username>"
    password = "<password>"

    fl = arcrest.agol.layer.FeatureLayer(url=url, username=username, password=password)

    features = arcrest.agol.common.Feature.fc_to_features(fc)
	
	#json_data["feed"]["entry"] for y anadir
    print fl.addFeature(features=features)

except ValueError, e:
    print e

#launch featureservice2trigger
# node featureservice2trigger --clientId=0luUVke61tJEvonb --clientSecret=3dd989b1cccf492aa5772bee221fba9a --tag=promociones --tag=restaurantes --serviceUrl="http://services.arcgis.com/Q6ZFRRvMTlsTTFuP/arcgis/rest/services/BigOffer/FeatureServer/0" --notificationTemplate="Welcome to {{msg}}"

