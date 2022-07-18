import pandas as pd
import numpy as np
from nsepy import get_history as gh
from datetime import date

df_data = pd.read_csv('nifty500list.csv')
df_data_ticket_list = list(df_data['Symbol'].unique())
df_data_company_list = list(df_data['Company Name'].unique())
df_data_industry_list = list(df_data['Industry'].unique())

df = pd.DataFrame()
df['Symbol'] = None
df['Company Name'] = None
df['Industry'] = None
df['20'] = None
symbols_missing = []
for i in range(0, len(df_data_ticket_list)):
    try:
        sym = df_data_ticket_list[i]
        df1 = gh(symbol= df_data_ticket_list[i], start=date(2022,4,4), end=date(2022,5,5))
        df1['next_20'] = df1['Close'].shift(-20)
        df1 = df1.iloc[0]
        pct_change = ((df1.next_20 - df1.Close)/df1.Close)*100
        pct_change = np.round(pct_change,2)
        #print(pct_change)
    except:
        symbols_missing.append(df_data_ticket_list[i])
        continue


# df['Symbol'] = df_data_ticket_list
# df['Company Name'] = df_data_company_list
# df['Industry'] = df_data_industry_list

# print(df)
print(symbols_missing)