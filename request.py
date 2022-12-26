from urllib.request import Request, urlopen, HTTPSHandler
from constants import BASE_URL, AUTHORISATION, AUTHORISATION_VALUE
import json

# Performs a network request and retrieves the output as a json object
def handle_request(endpoint) :
	request = Request(BASE_URL + endpoint)
	request.add_header(AUTHORISATION, AUTHORISATION_VALUE)
	request.timeout = 5000
	handler = HTTPSHandler()
	return json.loads(handler.https_open(request).read().decode("utf-8"))

# Gets all accounts for the given user access token and logs the Name, number of transations and Balance for them
def print_accounts() :	
	accounts = handle_request("/accounts")
	for val in accounts["data"] :
		id = val["id"]
		name = val["attributes"]["displayName"]
		balance = val["attributes"]["balance"]["value"]
		accountTransations = handle_request("/accounts/{}/transactions".format(id))
		print("Name: {}, Transactions: {}, Balance: {}".format(name, len(accountTransations["data"]), balance))

print_accounts()