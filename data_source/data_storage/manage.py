#Import libraries required
from data_source.data_load_api import info_stock_loader, historical_price_loader
from datetime import datetime
import ast
import os

def store_information_of_stock(update=False):
    if update:
        print('\n   Loading information of stock data...')
        df_info = info_stock_loader.info_stock_loader()
        os.makedirs('data_source/data_storage', exist_ok=True)
        df_info.to_csv('data_source/data_storage/information_of_stock.csv', encoding='utf-8-sig', index=False)
        print('\n       Saved successfully! information_of_stock.csv is updated at:', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    else:
        print('\n       Not update information_of_stock.csv!')

def store_historical_price(update=True, pages=15):
    if update:
        print('\n   Loading historical price...')
        df_price = historical_price_loader.load_price(pages)
        try:
            os.makedirs('data_source/data_storage', exist_ok=True)
            df_price.to_csv('data_source/data_storage/historical_price.csv', index=False)
        except Exception:
            return str(Exception)
        print('\n       Saved successfully! historical_price.csv is updated at:', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    else:
        print('\n       Not update historical price.csv!')

def store_marketcap(update=True, pages=21):
    if update:
        print('\n   Loading marketcap...')
        df_marketcap = historical_price_loader.load_marketcap(pages)
        try:
            os.makedirs('data_source/data_storage', exist_ok=True)
            df_marketcap.to_csv('data_source/data_storage/marketcap.csv', index=False)
        except Exception:
            return str(Exception)
        print('\n       Saved successfully! marketcap.csv is updated at:', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    else:
        print('\n       Not update marketcap.csv')
#Run as script
if __name__ == '__main__':
    info_stock = ast.literal_eval(input('Update information_of_stock table? (True/False) '))
    price = ast.literal_eval(input('Update historical_price table? (True/False) '))
    hpages = int(input('How many pages update of historical price? (100.000 elements/page | 15 + n)'))
    marketcap = ast.literal_eval(input('Update marketcap table? (True/False) '))
    mpages = int(input('How many pages update of marketcap? (100.000 elements/page | 21 + n)'))
    print('Start time:', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    store_information_of_stock(info_stock)
    store_historical_price(price, hpages)
    store_marketcap(marketcap, mpages)