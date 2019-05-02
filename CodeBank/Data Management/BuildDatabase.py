import re
from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults,GetUpdatedPropertyDetails



f_name = open("CompleteAddress.txt", "r")
data_base= open("UpdatedHomeLatLong.txt","+w")
write_out="street_address | zipcode | zillow_id | Zestimate | Home_type | num_bath | num_bed | home_size | Lat | Long "
data_base.write(write_out)

for line in f_name:
	line=line.rstrip("\n")
	address=line
	try:
		street_address=re.search("(.*?)(?<=CO)",address)
		street_address=street_address.group(0)
		zipcode=re.search("(?<=CO )(.*?)(?=,)", address)
		zipcode=zipcode.group(0)

		#!Get information from first zillow call
		zillow_data = ZillowWrapper(zws_id)
		deep_search_response = zillow_data.get_deep_search_results(street_address,zipcode)
		result = GetDeepSearchResults(deep_search_response)
		
		#!!The following will be stored as values in database
		Home_type=result.home_type
		Zestimate=result.zestimate_amount
		zillow_id=result.zillow_id
		lat=str(result.latitude)
		long_res=str(result.longitude)

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







