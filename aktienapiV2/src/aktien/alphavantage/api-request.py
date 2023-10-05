import requests

class Api_access:

    def __init__(self, api_key):
        self.api_key = api_key

    def get_monthly(self, symbol):
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=' + symbol + '&apikey=' + self.api_key
        r = requests.get(url)
        return r.json()
    
class API_utility:

    def __init__(self, api_key):
        self.api_key = api_key
        self.api = Api_access(api_key)
    
    def get_aktienbylist(self, symbol_list):
        aktien = []
        for symbol in symbol_list:
            aktien.append(self.get_aktie(symbol))
        return aktien
    

class Datenverarbeitung:

    def __init__(self):
        pass

