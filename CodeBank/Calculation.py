import requests 
import json
import random

#Sample Risk Assesment
#These are currently based on Zestimate numbers, which has no indication of risk. Will eventually replace with a fair risk assesment, and assign a number or symbol based off of that assesment
def getRisk(zillow_id):
	parameters = zillow_id
	base_url = base_url = "http://127.0.0.1:5002/Zestimate/"
	url = ''.join([base_url, parameters])
	result = result = requests.get(url)
	returns = json.loads(result.text)
	riskAssessment = returns[0]['Zestimate']
	if riskAssessment < 500000:
		return random.randint(1,3)
	else:
		return random.randint(3,6)

def getZestimate(zillow_id):
	parameters = zillow_id
	base_url = base_url = "http://127.0.0.1:5002/Zestimate/"
	url = ''.join([base_url, parameters])
	result = result = requests.get(url)
	returns = json.loads(result.text)
	return ("$%d" %returns[0]["Zestimate"])




