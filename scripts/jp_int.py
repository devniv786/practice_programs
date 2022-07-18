import pandas as pd
import  pyodbc

def calculate_length(x):
    return len(x)


input_file = input('Enter file name to load')
rules = input('Enter rules for column based on maximum length in key value format')
rules_list = rules.split(',')
rules_dict = {record.split(':')[0]:record.split(':')[1] for record in rules_list}
df = pd.read_csv(input_file,index_col='AsofDate')
for column in rules_dict.keys():
try:
    length_col = rules_dict[column]
    df[f'Len_{column}'] = df[column].apply(lambda x: calculate_length(x))
    temp_df = df[df[f'Len_{column}']>length_col
    if(temp_df.shape[0]>0):
        raise Exception
    else:
        continue

except Exception:
    print('Rule violated for column {}'.format(column))

else:
    db_obj = pyodbc.connect()







