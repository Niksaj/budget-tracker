import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.up.com.au/api/v1"
AUTHORISATION = "Authorization"
API_KEY = os.getenv("UP_API_KEY")
AUTHORISATION_VALUE = "Bearer {}".format(API_KEY)