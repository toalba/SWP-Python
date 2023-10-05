import requests

class Api_access:

    def __init__(self, api_key):
        self.api_key = api_key

    def get_monthly(self, symbol):
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=' + symbol + '&apikey=' + self.api_key
        r = requests.get(url)
        return r.json()