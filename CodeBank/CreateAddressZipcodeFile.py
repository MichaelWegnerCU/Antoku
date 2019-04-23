from googlemaps import Client
###
import requests
f_name = open("../RentalList.txt", "r")
Address_out= open("CompleteAddress.txt","w+")
# # print(f.read())
#for address in file_name:

gmaps = Client("AIzaSyC0IuivzVdNQnYQ0kIcZ7x_an7bJ7BwC3o")

# 
# #print(result)
# placemark = result[0]
# print()
#f_test=["1529 Arapahoe Ave APT A, Boulder, CO"]

for line in f_name:
	line=line.rstrip("\n")
	address=line

	try:
		result = gmaps.geocode(address)
		placemark = result[0]
		for_address=placemark['formatted_address']
		for_address=for_address+"\n"
		Address_out.write(for_address)
	except:
		print("An error occured obtaining zip code")

Address_out.close()