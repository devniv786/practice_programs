import nsepython
import pandas as pd
import time
# from datetime import datetime
import datetime
import logging

pd.set_option("max_colwidth", 1000)
pd.set_option('max_columns', 50)

logger = logging.getLogger()
logger.setLevel(logging.NOTSET)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler_format = '%(asctime)s | %(levelname)s: %(message)s'
console_handler.setFormatter(logging.Formatter(console_handler_format))
logger.addHandler(console_handler)

market_end_time = datetime.time(15, 40, 0)
market_start_time = datetime.time(9, 15, 0)
market_flag = True
expiry_date = '20-Jan-2022'
interval = 300
oi_dict = {'Time': [], 'Call OI': [], 'Put OI': [], 'Difference_in_OI': [], 'Nifty Spot': [], 'Call_Strikes':[], \
           'Call_IV':[], 'Call_LTPs':[], 'Put_Strikes':[], 'Put_IV':[], 'Put_LTPs':[]}
# current_time = datetime.today()

while(market_flag):
    current_time = datetime.datetime.today()
    # if (f'{current_time.hour}:{current_time.minute}:{current_time.second}' < market_end_time):
    try:
        if (datetime.time(current_time.hour, current_time.minute, current_time.second) < market_end_time):
            option_chain = nsepython.option_chain('NIFTY')
            option_chain = [record for record in option_chain['records']['data'] if record['expiryDate']==expiry_date]
            nifty_spot = float((nsepython.nse_get_index_quote('NIFTY 50')['last']).replace(',',''))
            df = pd.DataFrame(option_chain)
            df_ce = df[['CE']]
            df_pe = df[['PE']]

            df_ce_final = df_ce['CE'].apply(pd.Series)
            df_pe_final = df_pe['PE'].apply(pd.Series)

            df_ce_final = df_ce_final[df_ce_final['strikePrice'] >= int(nifty_spot - nifty_spot % 50)][:6]
            df_pe_final = df_pe_final[df_pe_final['strikePrice'] <= int(nifty_spot - nifty_spot % 50)].tail(6)
            df_ce_final = df_ce_final[['strikePrice', 'openInterest', 'impliedVolatility', 'lastPrice']]
            df_pe_final = df_pe_final[['strikePrice', 'openInterest', 'impliedVolatility', 'lastPrice']]
            call_oi = df_ce_final['openInterest'].sum()
            put_oi = df_pe_final['openInterest'].sum()
            diff_oi = call_oi - put_oi if call_oi > put_oi else put_oi - call_oi

            oi_dict['Call OI'].append(call_oi)
            oi_dict['Put OI'].append(put_oi)
            oi_dict['Difference_in_OI'].append(diff_oi)
            oi_dict['Time'].append(f'{current_time.hour}:{current_time.minute}')
            oi_dict['Nifty Spot'].append(nifty_spot)

            oi_dict['Call_Strikes'].append(list(df_ce_final['strikePrice'].unique()))
            oi_dict['Call_IV'].append(list(df_ce_final['impliedVolatility'].values))
            oi_dict['Call_LTPs'].append(list(df_ce_final['lastPrice'].values))

            oi_dict['Put_Strikes'].append(list(df_pe_final['strikePrice'].unique()))
            oi_dict['Put_IV'].append(list(df_pe_final['impliedVolatility'].values))
            oi_dict['Put_LTPs'].append(list(df_pe_final['lastPrice'].values))

            logger.info('Total Call OI: {:,}'.format(call_oi))
            logger.info('Total Put OI: {:,}'.format(put_oi))
            logger.info(f'Change in OI: {call_oi - put_oi if call_oi > put_oi else put_oi - call_oi}')
            logger.info(f'Nifty Spot: {nifty_spot}')

            # print(f'Total Call OI: {call_oi}')
            # print(f'Total Put OI: {put_oi}')
            # print(f'Change in OI: {call_oi - put_oi}')
            # print(f'Nifty Spot: {nifty_spot}')

            time.sleep(interval)

        else:
            market_flag = False
            df_oi_data = pd.DataFrame(oi_dict, columns=['Time', 'Call OI', 'Put OI', 'Difference_in_OI', 'Nifty Spot', \
                                                        'Call_Strikes', 'Call_IV', 'Call_LTPs', 'Put_Strikes', 'Put_IV', \
                                                        'Put_LTPs'])
            df_oi_data['Date'] = f'{current_time.day}-{current_time.month}-{current_time.year}'
            # df_oi_data = df_oi_data[['Date', 'Time', 'Call OI', 'Put OI', 'Difference_in_OI', 'Nifty Spot']]
            df_call_strikes = pd.DataFrame(df_oi_data['Call_Strikes'].tolist(),
                                           columns=['SP1_Call', 'SP2_Call', 'SP3_Call', 'SP4_Call', 'SP5_Call',
                                                    'SP6_Call'])
            df_call_prices = pd.DataFrame(df_oi_data['Call_LTPs'].tolist(),
                                          columns=['SP1_Call_Price_', 'SP2_Call_Price', 'SP3_Call_Price',
                                                   'SP4_Call_Price', 'SP5_Call_Price', 'SP6_Call_Price'])
            df_call_iv = pd.DataFrame(df_oi_data['Call_IV'].tolist(),
                                      columns=['SP1_Call_IV', 'SP2_Call_IV', 'SP3_Call_IV', 'SP4_Call_IV',
                                               'SP5_Call_IV', 'SP6_Call_IV'])
            df_put_strikes = pd.DataFrame(df_oi_data['Put_Strikes'].tolist(),
                                          columns=['SP1_Put', 'SP2_Put', 'SP3_Put', 'SP4_Put', 'SP5_Put', 'SP6_Put'])
            df_put_prices = pd.DataFrame(df_oi_data['Put_LTPs'].tolist(),
                                         columns=['SP1_Put_Price_', 'SP2_Put_Price', 'SP3_Put_Price', 'SP4_Put_Price',
                                                  'SP5_Put_Price', 'SP6_Put_Price'])
            df_put_iv = pd.DataFrame(df_oi_data['Put_IV'].tolist(),
                                     columns=['SP1_Put_IV', 'SP2_Put_IV', 'SP3_Put_IV', 'SP4_Put_IV', 'SP5_Put_IV',
                                              'SP6_Put_IV'])
            df_oi_data = df_oi_data[['Date', 'Time', 'Call OI', 'Put OI', 'Difference_in_OI', 'Nifty Spot']]
            df_oi_call_data_temp = df_call_strikes.merge(df_call_prices, left_index=True, right_index=True).merge(
                df_call_iv, left_index=True, right_index=True)
            df_oi_put_data_temp = df_put_strikes.merge(df_put_prices, left_index=True, right_index=True).merge(
                df_put_iv, left_index=True, right_index=True)
            df_call_put_final = df_oi_call_data_temp.merge(df_oi_put_data_temp, left_index=True, right_index=True)
            df_oi_data = df_oi_data.merge(df_call_put_final, left_index=True, right_index=True)

            try:
                df_oi = pd.read_csv('OI_Data.csv')
                df_oi = pd.concat([df_oi, df_oi_data], axis=0)
                df_oi.to_csv('OI_Data.csv', index=False)
            except FileNotFoundError:
                # df_oi_data = pd.DataFrame(oi_dict, columns=['Date', 'Time', 'Call OI', 'Put OI', 'Difference_in_OI'])
                # df_oi_data['Date'] = f'{current_time.day}:{current_time.month}:{current_time.year}'
                df_oi_data.to_csv('OI_Data.csv', index=False)

    except KeyError:
        continue
