from urllib.request import Request, urlopen
from constants import BASE_URL, AUTHORISATION, AUTHORISATION_VALUE

# Basic request to get account information and log that to the console
request = Request(BASE_URL + "/accounts")
request.add_header(AUTHORISATION, AUTHORISATION_VALUE)
contents = urlopen(request).read()
print(contents)