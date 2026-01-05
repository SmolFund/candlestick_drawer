# Core File
import requests
import time
import pandas as pd 
import mplfinance as mpf

class CandleStickCore():
    def __init__(self, symbol, timeframe, resolution):
        self.symbol = symbol
        self.timeframe = timeframe - (24 * 60 * 60)
        self.to_timeframe = timeframe
        self.resolution = resolution
    
    def get_data_from_nobitex(self):

        params = {
        "symbol": self.symbol,
        "resolution": self.resolution,
        "from": self.timeframe,
        "to": self.to_timeframe
        }

        base_url = f"https://apiv2.nobitex.ir/market/udf/history?symbol={params['symbol']}&resolution={params['resolution']}&from={params['from']}&to={params['to']}"

        res = requests.get(base_url)

        if res.ok:
            return res.json()
        else:
            return res.status_code
    
    def chart_to_file(self):
        chart_data = self.get_data_from_nobitex()

        df = pd.DataFrame({
            'Date': pd.to_datetime(chart_data['t'], unit='s'),
            'Open': chart_data['o'],
            'High': chart_data['h'],
            'Low': chart_data['l'],
            'Close': chart_data['c'],
            'Volume': chart_data['v']
        })


        return df