"""
Created on Wednesday Apri 17th
@author: Michael Wegnerr
@brief: Returns a list of all current rental properties in Boulder
@return: Lsit of rental properties

"""
# importing the requests library 
import requests
import xmltodict
from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults,GetUpdatedPropertyDetails
from collections import OrderedDict
ZILLOW_API_KEY= ""

address = '890 18th St Boulder, CO 80302'
zipcode = '80302'

zillow_data = ZillowWrapper(ZILLOW_API_KEY)
deep_search_response = zillow_data.get_deep_search_results(address,zipcode)
result = GetDeepSearchResults(deep_search_response)
zillow_id=result.zillow_id


# api-endpoint 
URL = "http://www.zillow.com/webservice/GetZestimate.htm"

zws_id=ZILLOW_API_KEY
zpid=zillow_id
rentzestimate=True

  
# defining a params dict for the parameters to be sent to the API 
PARAMS = {'zws-id':zws_id,'zpid':zpid,'rentzestimate':rentzestimate}
  
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


print("Current low Rent Zestimate:",low_rent_zestimate)
print("Current high Rent Zestimate:",high_rent_zestimate)
print("Current Rent Zestimate:",cur_rent_zestimate)




