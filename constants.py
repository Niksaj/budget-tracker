import os
from dotenv import load_dotenv

# This contents of this file were generated by ChatGPT after feeding in the original 
# file and asking it to simplify the code. 

# Constants
BASE_URL = "https://api.up.com.au/api/v1"
AUTHORISATION = "Authorization"
DATE_TIME_FORMAT = "%d-%m-%Y %H-%M-%S"
EXPORT_DIRECTORY = "output/"
PAGE_SIZE = 100
ENV_UP_KEY = "UP_API_KEY"

# Load environment variables
load_dotenv()

# Get API Key
API_KEY = os.environ.get(ENV_UP_KEY)
if API_KEY is None:
    API_KEY = input("Please enter your UP API key (this can be created here: https://developer.up.com.au/): ")
    os.environ[ENV_UP_KEY] = API_KEY

AUTHORISATION_VALUE = "Bearer {}".format(API_KEY)
