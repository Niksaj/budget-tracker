from constants import BASE_URL
from request import handle_request
import os

def validate_key() :
	success, _ = handle_request(BASE_URL + "/util/ping")
	if not success : 
		print("Failed to connect with the provided key, check your key and try again.")
		os.remove(".env")
		exit()

	print("Successfully connected with your key.")