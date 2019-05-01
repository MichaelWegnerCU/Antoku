##This file builds the primary address table for Boulder CO. Will contain only fully completed no null entry homes

import re
from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults,GetUpdatedPropertyDetails
import csv, sqlite3

def generate_Comp_fields_txt():
	zws_id= "X1-ZWz1h11b99c5qj_7kib9"

	f_name = open("UpdatedHomeLatLong.txt", "r")

	data_base= open("OnlyCompFields.txt","+w")

	write_out="street_address | zipcode | zillow_id | Zestimate | Home_type | num_bath | num_bed | home_size | Lat | Long | img url | home description "
	data_base.write(write_out)
	#f_name=["2893 Springdale Ln, Boulder, CO|80303|13239207|630640|Townhouse|3.5|1|1297|40.009373|-105.255454"]
	x=0
	for line in f_name:
		line=line.rstrip("\n")
		address=line
		if x==100:
			break
		try:
			street_address=re.search("(.*?)(?<=CO)",address)
			street_address=street_address.group(0)
			zipcode=re.search("(?<=CO\|)(.*?)(?=\|)", address)
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

			#######CALL TO UPDATED HOME DETAILS
			zillow_data = ZillowWrapper(zws_id)
			updated_property_details_response = zillow_data.get_updated_property_details(zillow_id)
			result = GetUpdatedPropertyDetails(updated_property_details_response)
			photo_gall=result.photo_gallery
			home_d=result.home_description

			write_out=street_address+'|'+zipcode+"|"+zillow_id+"|"+Zestimate+"|"+num_bath+"|"+num_bed+"|"+lat+"|"+long_res+"\n"
			print(str(write_out))
			data_base.write(write_out)
			x+=1
			
		except:
			print("Nothing Added")

	#f_name.close()
	data_base.close()

generate_Comp_fields_txt()

def generate_only_comp_fields_db():
	conn = sqlite3.connect("OnlyComp.db")
	curs = conn.cursor()
	curs.execute("CREATE TABLE Address (street_address TEXT, zipcode INTEGER, zillow_id INTEGER PRIMARY KEY, Zestimate INTEGER, HomeType TEXT, NumBath INTEGER, NumBed INTEGER, HomeSize INTEGER, LNG REAL, LAT REAL, PhotoLink Text, HomeDescription Text);")
	reader = csv.reader(open('OnlyCompFields.txt', 'r'), delimiter='|')
	for row in reader:

		print(row)#
		to_db = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]]
		curs.execute("INSERT INTO Address (street_address, zipcode, zillow_id, Zestimate, NumBath, NumBed, LNG, LAT) VALUES (?, ?, ?, ?, ?, ?, ?, ?);", to_db)
	conn.commit()

generate_only_comp_fields_db()

def testing():
	import os
	import urllib.request  as urllib2 
	from urllib.request import urlretrieve
	from bs4 import BeautifulSoup

	url = "https://www.zillow.com/homedetails/3375-Chisholm-Trl-A304-Boulder-CO-80301/13223169_zpid/#image=lightbox%3Dtrue"
	html = urllib2.urlopen(url)
	soup = BeautifulSoup(html)
	print(soup)

	imgTag = soup.findAll("img", {"class": "photo-tile-image"})
	print(imgTag)
	imgSrc = imgTag[0] # in this case, the source is the full url
	
	# but in other cases it may be relative path, in which case you would append it
	# to the base url
	urlretrieve(imgSrc,filename="testg.jpg")


	



