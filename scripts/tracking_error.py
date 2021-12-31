import math
import pandas as pd


df_nifty = pd.read_csv(r'C:\Users\10678727\Core Python\Re__Python_Assignment\NIFTY-TotalReturnsIndex.csv')
df_hdfc = pd.read_excel(r'C:\Users\10678727\Core Python\Re__Python_Assignment\HDFC Nifty ETF.xlsx')
df_kotak = pd.read_excel(r'C:\Users\10678727\Core Python\Re__Python_Assignment\Kotak Nifty ETF.xlsx')

df_nifty['Daily Return_Nifty'] = df_nifty['Close'].pct_change()
df_nifty['Date'] = pd.to_datetime(df_nifty['Date'], infer_datetime_format=True)
df_hdfc['Daily Return_HDFC'] = df_hdfc['Close'].pct_change()
df_kotak['Daily Return_Kotak'] = df_kotak['NAV'].pct_change()

df_final_data = df_nifty.merge(df_kotak, left_on = 'Date', right_on='Date').merge(df_hdfc, left_on='Date', right_on='Date')
df_final_data = df_final_data[['Date',  'Daily Return_Nifty', 'Daily Return_Kotak', 'Daily Return_HDFC']]
df_final_data.rename({'Daily Return':'Daily Return_HDFC'}, inplace=True)
df_final_data['Year'] = df_final_data['Date'].dt.year

def calculate_tracking_error(year, fund):
    df_temp = df_final_data[df_final_data['Year']==year]
    df_temp.set_index('Date', inplace=True)
    df_temp = df_temp[[col for col in df_temp.columns if(col.__contains__(fund) or col.__contains__('_Nifty'))]]
    df_temp['Diff'] = df_temp['Daily Return_Nifty'] - df_temp['Daily Return_'+ fund]
    df_temp['Diff'] = df_temp['Diff'].apply(lambda x : math.pow(x, 2))
    tracking_error = math.sqrt(df_temp['Diff'].sum() / (df_temp.shape[0] - 1))
    return tracking_error

funds = ['Kotak', 'HDFC']
years = [2016, 2017]
tracking_dict = {}
for year in years:
    tracking_dict[year] = dict()
    for fund in funds:
        te = calculate_tracking_error(year, fund)
        tracking_dict[year].update({fund:te})

print(tracking_dict)

df_tracking_error = pd.DataFrame(tracking_dict)
df_tracking_error.reset_index(inplace=True)
df_tracking_error.rename(columns={'index':'Fund'}, inplace=True)
df_tracking_error = df_tracking_error.melt(id_vars='Fund', value_vars=[2016, 2017], value_name='Tracking Error', var_name='Year')
df_tracking_error.sort_values(by=['Year','Tracking Error'], inplace=True)
print(df_tracking_error)