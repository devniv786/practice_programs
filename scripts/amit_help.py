import pandas as pd
import numpy as np
import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt
import pandas_datareader as web
import warnings

warnings.filterwarnings('ignore')

# importing the necessary library
from concurrent import futures

stocksList = ['RELIANCE.NS','INFY.NS','KOTAKBANK.NS','ICICIBANK.NS','TCS.NS', 'HDFCBANK.NS', 'HDFC.NS', 'LT.NS', 'HINDUNILVR.NS', 'BAJFINANCE.NS']

list_stocks = []

### Keeping track of failed ticker download queries
bad_tickers = []

end = dt.date(2017, 12, 31)
start = dt.date(2016, 1, 1)

def download_stocks(stock):
    try:
        print('Trying to retrieve the %s symbol...\n' % (stock))
        stock_df = web.DataReader(stock, 'yahoo', start, end)
        stock_df['Name'] = stock
        output_name = stock + '.csv'
        list_stocks.append(output_name)
        stock_df.to_csv(output_name)
        print('Symbol %s downloaded OK.\n' % (stock))
    except:
        bad_tickers.append(stock)
        print('Problems downloading the %s symbol.\n' % (stock))


# We use the concurrent.futures module's ThreadPoolExecutor
# to speed up the downloads by doing them in parallel rather than serially

### Set the maximum thread number
max_workers = 50

workers = min(max_workers, len(stocksList))
### In case a smaller number of stocks than threads was passed in
with futures.ThreadPoolExecutor(workers) as executor:
    res = executor.map(download_stocks, stocksList)
### map allows multiple calls to the given function. It passes each of the items in stocksList (any
### iterable) to the function. Here, it can happen concurrently because of the ThreadPoolExecutor()
### subClass

# A function to take in a stock symbol, reads saved data from the csv file & returns a dataframe containing its daily returns.
def returns_calculator(stock):
    stock_df = pd.read_csv(stock + '.csv',index_col='Date')
    stock_df[stock+'_daily_return'] = np.log(stock_df['Close']/stock_df['Close'].shift(1))
    stock_Ret = pd.DataFrame(stock_df[stock+'_daily_return'])
    return(stock_Ret)


# create a Series
pd.Series(stocksList)

# apply the returns_calculator() to each element of the series and save the new Series in "res"
res = pd.Series(stocksList).apply(returns_calculator)

# Each value in the 'res' Series is a DataFRame of returns

# Creating an empty dataframe called "result"
result=pd.DataFrame()

# taking individual dataframes (each stock) and concatanating it to empty df result on the column axis
for i in res:
    result = pd.concat([i,result],axis=1)

result.head()

##Daily portfolio returns = sum of (weightings on each stock * returns). Since, weightings here are same on all stocks i.e. 10%,
## daily portfolio returns = 0.1 * (Sum of returns of each stock)
result["daily_portfolio_returns"] = 0.1*(result.sum(axis=1))
result.head()
result.index = pd.to_datetime(result.index)

##Read Nifty ETF and Junior ETF data
nifty_etf = pd.read_excel("Nifty ETF.xlsx", index_col='Date')
junior_etf = pd.read_excel("Junior ETF.xlsx", index_col='Date')
nifty_etf["nifty_daily_returns"]= np.log(nifty_etf["Close"]/nifty_etf["Close"].shift(1))
junior_etf["junior_daily_returns"]= np.log(junior_etf["Close"]/junior_etf["Close"].shift(1))

#Creating dictionary with required returns data of portfolio, nifty ETF and junior ETF
data = {'Portfolio Returns':result['daily_portfolio_returns'], 'Nifty ETF Returns':nifty_etf['nifty_daily_returns'],
        'Junior ETF Returns':junior_etf['junior_daily_returns']}

df = pd.DataFrame(data)
df.head()