from googlemaps import Client

address = '1934 18th St, Boulder, CO'

gmaps = Client("AIzaSyC0IuivzVdNQnYQ0kIcZ7x_an7bJ7BwC3o")

result = gmaps.geocode(address)
#print(result)
placemark = result[0]
print(placemark['address_components'][7]['long_name'])


f = open("RentalList.txt", "r")
print(f.read())

for address in file_name:
	