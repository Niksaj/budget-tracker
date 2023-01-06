from urllib.request import Request, HTTPSHandler
from constants import AUTHORISATION, AUTHORISATION_VALUE
import json

# Performs a network request and retrieves the output as a json object
def handle_request(url) :
	request = Request(url)
	request.add_header(AUTHORISATION, AUTHORISATION_VALUE)
	request.timeout = 5000
	handler = HTTPSHandler()
	response = handler.https_open(request)
	code = response.getcode()
	return code >= 200 and code < 300, json.loads(response.read().decode("utf-8"))