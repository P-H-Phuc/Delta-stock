"""GET HISTORY PRICE AND MARKETCAP OF SYMBOLS"""

#Call packages
import timeit
from data_source import helpers
import pandas as pd

import itertools

SYMBOLS = helpers.get_symbols()

#Side function

def do_price(page):
      headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
      x = helpers.get_api(f'https://finfo-api.vndirect.com.vn/v4/stock_prices?sort=date:desc&q=floor:HOSE,HNX~type:STOCK&fields=code,date,open,high,low,close,nmVolume,change,pctChange&size=100000&page={page}', 
                          headers=headers) 
      return x

#Side function

def do_market(page):
      headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
      x = helpers.get_api(f'https://finfo-api.vndirect.com.vn/v4/ratios?sort=reportDate&fields=code,reportDate,value&q=itemCode:51003~group:stock&size=100000&page={page}',
                          headers=headers)
      return x

#Main function

def load_price(lastpage = 15):
      a = list(map(do_price, range(1, lastpage+1)))
      b = list(itertools.chain.from_iterable(a))
      df = pd.DataFrame.from_dict(b)
      df = df.rename(columns={'code': 'symbol'})
      df = df[df['symbol'].isin(SYMBOLS)]
      df = df[['symbol', 'date', 'open', 'high', 'low', 'close', 'change', 'pctChange', 'nmVolume']]
      return df.sort_values(by=['symbol', 'date']).reset_index(drop=True)
      
#Main function

def load_marketcap(lastpage=21):
      a = list(map(do_market, range(1, lastpage+1)))
      b = list(itertools.chain.from_iterable(a))
      df = pd.DataFrame.from_dict(b)
      df = df.rename(columns={'code': 'symbol', 'reportDate': 'date', 'value': 'marketCap'})
      df = df[df['symbol'].isin(SYMBOLS)]
      return df.sort_values(by=['symbol', 'date']).reset_index(drop=True)

#Run as script
if __name__ == '__main__':
      x = int(input('How many pages update of historical price?'))
      y = int(input('How many pages update of marketcap?'))
      print('Loading...')
      s = timeit.default_timer()
      load_price(x).info()
      load_marketcap(y).info()
      print('Time run:', timeit.default_timer() - s)