from urllib.request import Request, HTTPSHandler
from constants import BASE_URL, AUTHORISATION, AUTHORISATION_VALUE
import json

# Performs a network request and retrieves the output as a json object
def handle_request(endpoint) :
	request = Request(BASE_URL + endpoint)
	request.add_header(AUTHORISATION, AUTHORISATION_VALUE)
	request.timeout = 5000
	handler = HTTPSHandler()
	return json.loads(handler.https_open(request).read().decode("utf-8"))