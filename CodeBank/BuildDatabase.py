import re
from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults,GetUpdatedPropertyDetails

zws_id= "X1-ZWz1h11b99c5qj_7kib9"

f_name = open("CompleteAddress.txt", "r")
data_base= open("lat_test.txt","+w")
write_out="street_address | zipcode | zillow_id | Zestimate | Home_type | num_bath | num_bed | home_size"
data_base.write(write_out)

f_name=["2893 Springdale Ln, Boulder, CO 80303, USA","3000 Broadway #2, Boulder, CO 80304, USA","1623 19th St, Boulder, CO 80302, USA"]

for line in f_name:
	line=line.rstrip("\n")
	address=line
	street_address=re.search("(.*?)(?<=CO)",address)
	street_address=street_address.group(0)
	zipcode=re.search("(?<=CO )(.*?)(?=,)", address)
	zipcode=zipcode.group(0)

	try:
		#!Get information from first zillow call
		zillow_data = ZillowWrapper(zws_id)
		deep_search_response = zillow_data.get_deep_search_results(street_address,zipcode)
		result = GetDeepSearchResults(deep_search_response)
		
		#!!The following will be stored as values in database
		Home_type=result.home_type
		Zestimate=result.zestimate_amount
		zillow_id=result.zillow_id
		lat=result.latitude
		long_res=result.longitude

		num_bath=str(result.bathrooms)
		num_bed=str(result.bedrooms)
		home_size=str(result.home_size)
		write_out=street_address+'|'+zipcode+"|"+zillow_id+"|"+Zestimate+"|"+Home_type+"|"+num_bath+"|"+num_bed+"|"+home_size+"|"+lat+"|"+long_res+"\n"
		print(str(write_out))
		data_base.write(write_out)
		
	except:
		print("Nothing Added")

#f_name.close()
data_base.close()







