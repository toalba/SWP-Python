from typing import Any
from aktien.alphavantage.db import connection

class Depiction:

    def output(self, data):
        # output looks like this: {2023: [(46.69, -216.41, 263.1), (0, 0, 0)], 2022: [(-57.02, -268.13, 211.11), (51.59, -169.03, 220.62)], 2021: [(82.49, -143.24, 225.73), (32.5, -205.97, 238.47)]
        # 2023: [(46.69, -216.41, 263.1), (0, 0, 0)] -> 2023: [ab,xy]
        # print in terminal
        print(f'YYYY | Close_SEP - Open_JAN SPY as A| Close_SEP - Open_JAN IWM as B| A-B | Close_DEZ - Open SEP SPY as X | Close_DEZ - Open SEP IWM as Y |  X-Y')
        for year,values in data.items():
            print(f'{year} | {values[0][0]} | {values[0][1]} | {values[0][2]} | {values[1][0]} | {values[1][1]} | {values[1][2]}')
            print('------------------------------------------------------------------------')
        # create plot
        import matplotlib.pyplot as plt
        import numpy as np
        # create data
        x = []
        y = []
        for year,values in data.items():
            x.append(values[0][2])
            y.append(values[1][2])
        
        # create plot
        fig, ax = plt.subplots()
        ax.scatter(x, y)
        ax.set_xlabel('A-B')
        ax.set_ylabel('X-Y')
        ax.set_title('Scatter plot')
        plt.show()
        
        
    



class Calculation:

    def __init__(self, symbols):
        self.db = connection
        self.dataset = self.get_dataset(symbols)
        self.depiction = Depiction()

    def __call__(self):
        filtered_data = self.get_september_december_january()
        return self.calculate(filtered_data)

    def get_dataset(self, symbols):
        datasets = {}
        for symbol in symbols:
            datasets.update({symbol:connection.get_close_open_by_symbol(symbol)})
        return datasets
    
    # get for each year the september, december and january close and open for each symbol in dataset
    def get_september_december_january(self):
        filtered_data = {}
        for symbol,value in self.dataset.items():
            filtered = list(filter(lambda x: x[0].month in [9,12,1], value))
            # filter results by year
            def filter_by_year(year):
                return list(filter(lambda x: x[0].year == year, filtered))
            years = list(map(lambda x: filter_by_year(x[0].year), filtered))
            resyear = {}
            # remove duplicate year entries
            for year in years:
                resyear[year[0][0].year] = year
            filtered_data[symbol] = resyear
        return filtered_data
    
    def calculate(self,data):
        def calculate_open_close(open1,open2,close1,close2):
            # check if any value is 0
            if open1 == 0 or open2 == 0 or close1 == 0 or close2 == 0:
                return 0,0,0
            a = open1 - close2
            b = open2 - close1
            ab = a - b
            return round(a,2), round(b,2), round(ab,2)
        res = {}
        # Jahr | Close_SEP - Open_JAN SPY as A| Close_SEP - Open_JAN IWM as B| A-B | Close_DEZ - Open SEP SPY as X | Close_DEZ - Open SEP IWM as Y |  X-Y
        symbol1 = list(data.values())[0]
        symbol_keys = list(data.keys())
        symbol2 = list(data.values())[1]
        def get_december(value):
            a = list(filter(lambda x: x[0].month == 12, value))
            return a[0] if len(a) > 0 else None
        def get_september(value):
            a = list(filter(lambda x: x[0].month == 9, value))
            return a[0] if len(a) > 0 else None
        def get_january(value):
            a = list(filter(lambda x: x[0].month == 1, value))
            return a[0] if len(a) > 0 else None
        def getclose(value):
            return value[2] if value is not None else 0
        def getopen(value):
            return value[1] if value is not None else 0
        for year in symbol1.keys():
            # check if year exists in symbol2
            if year not in symbol2.keys():
                continue
            values = [symbol1[year],symbol2[year]]            
            ab = calculate_open_close(
                getclose(get_september(values[0])),
                getclose(get_september(values[1])),
                getopen(get_january(values[0])),
                getopen(get_january(values[0]))
            )
            xy = calculate_open_close(
                getclose(get_december(values[0])),
                getclose(get_december(values[1])),
                getopen(get_september(values[0])),
                getopen(get_september(values[0]))
            )
            res[year] = [ab,xy]
        return res
    

