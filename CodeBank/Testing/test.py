
import requests
from collections import OrderedDict
import xmltodict
import csv, sqlite3

zws_id= "X1-ZWz1h11b99c5qj_7kib9"
zpid = 2121254219
rentzestimate = True
count = 10

def get_rent_zet(zpid):
	PARAMS = {'zws-id':zws_id,'zpid':zpid,'count': count, 'rentzestimate':rentzestimate}
	URL = "http://www.zillow.com/webservice/GetComps.htm"
	r = requests.get(url = URL, params=PARAMS)
	data = r.content.decode('utf-8')
	xmltodict_data = xmltodict.parse(data)
	items=list(xmltodict_data.items())
	print (items)


get_rent_zet(zpid)