from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


# The url to the API for the data request
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

# What is needed
parameters = {
    'start':'1', # CMC Rank/ Crypto Choice
    'limit':'1', # Limit the data requested
    'convert':'ZAR'
}

# API validation so I can get access
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'API_KEY_GOES_HERE', # Get your api key from here https://coinmarketcap.com/api/
}

# Create a session
session = Session()

# Update the header by using the session
session.headers.update(headers)

try:
    # variable = get the url and parameters from the session
    response = session.get(url, params=parameters)

    # variable = loads the response as text from the json
    data = json.loads(response.text)

    # variable = list[main column][index of subcolumns][other column]
    name = data['data'][0]['name']
    quote = data['data'][0]['quote']['ZAR']['price']

    print("Name: " + str(name))
    print("Price: R" + str(quote))

except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

