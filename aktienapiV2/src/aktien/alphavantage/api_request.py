import requests
from aktien.alphavantage.db import DatabaseConction

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
            aktien.append(self.api.get_monthly(symbol))
        return aktien
    

class Datenverarbeitung:

    def __init__(self):
        self.connection = DatabaseConction()

    def set_aktien(self, aktien):
        for aktie in aktien:
            symbol = self.get_symbol(aktie)
            if self.connection.check_if_table_exists(symbol):
                self.connection.create_table(symbol)
            data = aktie['Monthly Time Series']
            dates = data.keys()
            cursor = self.connection.connection.cursor()
            update_count = 0
            for date in dates:
                if self.connection.check_if_key_exits_in_table(symbol, date):
                    continue
                res = cursor.execute(f"INSERT INTO {symbol} VALUES ('{date}', {data[date]['1. open']}, {data[date]['2. high']}, {data[date]['3. low']}, {data[date]['4. close']}, {data[date]['5. volume']})")
                update_count+1
            print(f'New Entries: {update_count}')
            self.connection.connection.commit()

    def get_symbol(self,aktie):
        return aktie['Meta Data']['2. Symbol']
