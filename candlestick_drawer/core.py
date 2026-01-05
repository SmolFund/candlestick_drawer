# Core File
import requests
import time
import pandas as pd 
import mplfinance as mpf

class CandleStickCore():
    def __init__(self, symbol, timeframe, resolution):
        self.symbol = symbol
        self.timeframe = timeframe
        self.to_timeframe = timeframe * 60 * 60 #hours to seconds, since we need 24 hours and above, the base is on 24 hours for now.
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

        return res