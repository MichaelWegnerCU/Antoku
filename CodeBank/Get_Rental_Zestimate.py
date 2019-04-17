import requests
import xmltodict
from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults,GetUpdatedPropertyDetails
from collections import OrderedDict
zws_id= "X1-ZWz1h11b99c5qj_7kib9"

address = '890 18th St Boulder, CO 80302'
zipcode = '80302'

zillow_data = ZillowWrapper(zws_id)

def get_rent_zest(address,zip):
	deep_search_response = zillow_data.get_deep_search_results(address,zipcode)
	result = GetDeepSearchResults(deep_search_response)

	zpid=result.zillow_id
	rentzestimate=True
	# defining a params dict for the parameters to be sent to the API 
	PARAMS = {'zws-id':zws_id,'zpid':zpid,'rentzestimate':rentzestimate}
	# api-endpoint 
	URL = "http://www.zillow.com/webservice/GetZestimate.htm"

	rentzestimate=True

	r = requests.get(url = URL, params = PARAMS) 
	#print(r.content)

	data = r.content.decode('utf-8')
	xmltodict_data = xmltodict.parse(data)
	items=list(xmltodict_data.items())

	def listRecursive (d, key, path = None):
	    if not path: path = []
	    for k, v in d.items ():
	        if isinstance (v, OrderedDict):
	            for path, found in listRecursive (v, key, path + [k] ):
	                yield path, found
	        if k == key:
	            yield path + [k], v

	for path, found in listRecursive (xmltodict_data, 'rentzestimate'):
	    rent_zest=found

	amount= dict(rent_zest)
	cur_rent_zestimate=dict(amount['amount'])['#text']
	low_rent_zestimate=dict(dict(amount['valuationRange'])['low'])['#text']
	high_rent_zestimate=dict(dict(amount['valuationRange'])['high'])['#text']
	return {'current':cur_rent_zestimate,'low':low_rent_zestimate,'high':high_rent_zestimate}







