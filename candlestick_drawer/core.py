# Core File
from uuid import uuid4
import requests
import time
import pandas as pd 
import mplfinance as mpf

class CandleStickCore():
    def __init__(self, symbol, timestamp, resolution, interval, timeframe):
        self.symbol = symbol
        self.timestamp = timestamp - (24 * 60 * 60)
        self.to_timestamp = timestamp
        self.resolution = resolution
        self.interval = interval
        self.timeframe = timeframe
    
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
    
    def chart_to_file(self, filename):
        chart_data = self.get_data_from_nobitex()

        df = pd.DataFrame({
            'Date': pd.to_datetime(chart_data['t'], unit='s'),
            'Open': chart_data['o'],
            'High': chart_data['h'],
            'Low': chart_data['l'],
            'Close': chart_data['c'],
            'Volume': chart_data['v']
        })

        cols = ['Open', 'High', 'Low', 'Close', 'Volume']
        df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')

        df.set_index('Date', inplace=True)

        mpf.plot(
            df, 
            type='candle', 
            style='charles', 
            title=f'\n{self.symbol} Last 24 Hours',
            ylabel='Price',
            volume=False,
            show_nontrading=False,
            savefig=dict(fname=f"{filename}.png", dpi=300, pad_inches=0.25)
        )

        return True