# Core File
import requests
import time
import pandas as pd 
import mplfinance as mpf

class CandleStickCore():
    def __init__(self, symbol, timeframe, resolution):
        self.symbol = symbol
        self.timeframe = timeframe * 60 * 60 #hours to seconds, since we need 24 hours and above, the base is on 24 hours for now.
        self.resolution = resolution
    
    def get_data_from_nobitex():
        params = {
        "symbol": symbol,
        "resolution": resolution,
        "from": from_timestamp,
        "to": to_timestamp
    }