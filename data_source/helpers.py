import functools
import requests
import pandas as pd

#Ignore unhashable
#More: https://stackoverflow.com/questions/49210801/python3-pass-lists-to-function-with-functools-lru-cache
def ignore_unhashable(func): 
    uncached = func.__wrapped__
    attributes = functools.WRAPPER_ASSIGNMENTS + ('cache_info', 'cache_clear')
    @functools.wraps(func, assigned=attributes) 
    def wrapper(*args, **kwargs): 
        try: 
            return func(*args, **kwargs) 
        except TypeError as error: 
            if 'unhashable type' in str(error): 
                return uncached(*args, **kwargs) 
            raise 
    wrapper.__uncached__ = uncached
    return wrapper

#Filter drivers
@ignore_unhashable
@functools.lru_cache
def filter_drivers(list_of_dicts, drivers):
    a = []
    for d in list_of_dicts:
        b = {i: d.get(i) for i in drivers}
        a.append(b)
    return a

#Get data from api
@ignore_unhashable
@functools.lru_cache
def get_api(api, headers={'User-Agent': 'Mozilla/5.0'}):
    page = requests.get(url=api, headers=headers)
    return page.json()['data']

#Get list of symbols
@ignore_unhashable
@functools.lru_cache
def get_symbols():
    jdata = get_api(api='https://finfo-api.vndirect.com.vn/v4/stocks?sort=code:asc&q=type:stock~floor:HOSE,HNX~status:listed&fields=code&size=1000')
    symbols = [symbol.get('code') for symbol in jdata]
    return symbols

#Get option for dropdown seach symbol
@functools.lru_cache
def dropdown_find():
    api = 'https://finfo-api.vndirect.com.vn/v4/stocks?sort=code:asc&q=type:stock~floor:HOSE,HNX~status:listed&fields=code,shortName&size=1000'
    list_of_dicts = get_api(api)
    option = []
    for i in list_of_dicts:
        d = {'label': f'{i.get("code")} - {i.get("shortName")}',
             'value': f'{i.get("code")}'}
        option.append(d)
    return option

#Call data------------------------------
df_information_of_stock = pd.read_csv('data_source/data_storage/information_of_stock.csv')
df_historical_price = pd.read_csv('data_source/data_storage/historical_price.csv')
df_marketcap = pd.read_csv('data_source/data_storage/marketcap.csv')

def get_information_of_(symbol):
    df = df_information_of_stock[df_information_of_stock['symbol'] == symbol]
    return df

def get_historical_price_of_(symbol, start_date, end_date):
    if isinstance(symbol, str):
        df = df_historical_price[df_historical_price['symbol'] == symbol]
    if isinstance(symbol, list):
        df = df_historical_price[df_historical_price['symbol'].isin(symbol)]
    df.index = pd.to_datetime(df['date'], format='%Y-%m-%d')
    df.index.name = 'index'
    df_filtered = df.sort_index().loc[start_date : end_date, :]
    return df_filtered

def get_marketcap_of_(symbol, start_date, end_date):
    if isinstance(symbol, str):
        df = df_marketcap[df_marketcap['symbol'] == symbol]
    if isinstance(symbol, list):
        df = df_marketcap[df_marketcap['symbol'].isin(symbol)]
    df.index = pd.to_datetime(df['date'], format='%Y-%m-%d')
    df.index.name = 'index'
    df_filtered = df.sort_index().loc[start_date : end_date, :]
    return df_filtered