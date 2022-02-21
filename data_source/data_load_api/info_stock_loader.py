"""LOAD INFORMATIONLOAD BASIC OF SYMBOLS"""

#Call packages
import timeit
import pandas as pd
from data_source import helpers

SYMBOLS = helpers.get_symbols()

#Main function
def info_stock_loader():
    #Set data
    df1, df2 = load1(), load2()
    df_main = pd.merge(df1,df2,on='symbol',how='inner')
    df_main = df_main[['symbol', 'companyName', 'companyNameEng',
                       'shortName', 'foundDate', 'phone', 'email',
                       'vnAddress', 'website', 'industryName',
                       'floor', 'listedDate', 'vnSummary']]
    return df_main

#Side function
def load1():
    list_of_dicts = helpers.get_api(api='https://finfo-api.vndirect.com.vn/stocks?status=listed&floor=HNX,HOSE')
    list_of_dicts = helpers.filter_drivers(list_of_dicts, drivers=['symbol', 'companyName', 'companyNameEng', 'shortName','listedDate','floor', 'industryName'])
    df = pd.DataFrame(list_of_dicts)
    #Only stock of company
    df = df[df['symbol'].isin(SYMBOLS)]
    return df
#Side function
def load2():
    list_of_dicts = helpers.get_api(api='https://finfo-api.vndirect.com.vn/v4/company_profiles?sort=code:asc&q=floor:HOSE,HNX&fields=code,vnAddress,phone,email,website,vnSummary,foundDate,&size=9999')
    df = pd.DataFrame(list_of_dicts)
    df = df.rename(columns={'code': 'symbol'})
    #Only stock of company
    df = df[df['symbol'].isin(SYMBOLS)]
    return df

#Run as script
if __name__ == '__main__':
      s = timeit.default_timer()
      x = info_stock_loader()
      x.info()
      print('\nTime run:', timeit.default_timer() - s)