import pandas as pd

df = pd.DataFrame({'ID':[1,1,3,2,2,3],'Date':['2022-01-01','2022-01-01','2022-01-01','2022-01-01','2022-01-01','2021-01-02'],
                   'Ticker':['IBM','GOOG','IBM','IBM','AAPL','META'],
                   'Units':[100,200,100,100,100,500]})

df_group = df.groupby(['ID','Date']).count()
# df_group = df.groupby(['ID','Date']).max()
print(df_group)
df_group.reset_index(inplace=True)

df_final = pd.DataFrame()
for date in list(df_group['Date'].unique()):
    max_securities = max(df_group[df_group['Date']==date]['Ticker'])
    df_temp = df_group[(df_group['Date']==date) & (df_group['Ticker']==max_securities)]
    df_final = pd.concat([df_final, df_temp], axis=0)
    print(max_securities)

print(df_final)




