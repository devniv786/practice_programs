import nsepython
import pandas as pd
import time
# from datetime import datetime
import datetime
import logging

logger = logging.getLogger()
logger.setLevel(logging.NOTSET)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler_format = '%(asctime)s | %(levelname)s: %(message)s'
console_handler.setFormatter(logging.Formatter(console_handler_format))
logger.addHandler(console_handler)

# market_end_time = '15:30:00'
market_end_time = datetime.time(15, 30, 0)
market_start_time = datetime.time(9, 15, 0)
# market_start_time = '9:15:00'
market_flag = True
# current_time = datetime.today()

while(market_flag):
    current_time = datetime.datetime.today()
    # if (f'{current_time.hour}:{current_time.minute}:{current_time.second}' < market_end_time):
    if (datetime.time(current_time.hour, current_time.minute, current_time.second) < market_end_time):
        option_chain = nsepython.option_chain('NIFTY')
        option_chain = [record for record in option_chain['records']['data'] if record['expiryDate']=='30-Dec-2021']
        nifty_spot = float((nsepython.nse_get_index_quote('NIFTY 50')['last']).replace(',',''))
        df = pd.DataFrame(option_chain)
        df_ce = df[['CE']]
        df_pe = df[['PE']]

        df_ce_final = df_ce['CE'].apply(pd.Series)
        df_pe_final = df_pe['PE'].apply(pd.Series)

        call_oi = df_ce_final['openInterest'].sum()
        put_oi = df_pe_final['openInterest'].sum()

        logger.info('Total Call OI: {:,}'.format(call_oi))
        logger.info('Total Put OI: {:,}'.format(put_oi))
        logger.info(f'Change in OI: {call_oi - put_oi if call_oi > put_oi else put_oi - call_oi}')
        logger.info(f'Nifty Spot: {nifty_spot}')

        # print(f'Total Call OI: {call_oi}')
        # print(f'Total Put OI: {put_oi}')
        # print(f'Change in OI: {call_oi - put_oi}')
        # print(f'Nifty Spot: {nifty_spot}')

        time.sleep(60)

    else:
        market_flag = False