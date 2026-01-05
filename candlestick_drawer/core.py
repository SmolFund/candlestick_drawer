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
            return res
        else:
            return res.status_code