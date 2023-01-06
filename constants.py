import os
from dotenv import load_dotenv

def get_key() :
	key = input("Please enter your UP API key (this can be created here: https://developer.up.com.au/): ")
	f = open(".env", "w")
	f.write("{}={}".format(ENV_UP_KEY, key))
	f.close()
	return key

# constants
BASE_URL = "https://api.up.com.au/api/v1"
AUTHORISATION = "Authorization"
DATE_TIME_FORMAT = "%d-%m-%Y %H-%M-%S"
EXPORT_DIRECTORY = "output/"
PAGE_SIZE = 100
ENV_UP_KEY = "UP_API_KEY"

# load evironment
LOADED_ENV = load_dotenv()

# environment constants
API_KEY = os.getenv(ENV_UP_KEY) if LOADED_ENV else get_key()
AUTHORISATION_VALUE = "Bearer {}".format(API_KEY)