import math

import pandas as pd
import json
import requests
import time


def myfirstfunction():
    print('hello HSLU !')


def get_dataset(filename):
    df = pd.read_csv(filename)
    return df


df_census = get_dataset('census.csv')
# print(df_census.head().to_string())
df_census.drop(['native-country'], axis=1, inplace=True)

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 22]
mylist2 = [('patricia', 6, 5), ('jose', 5, 5), ('Juan', 4, None)]

# for item in mylist:
#     print(item)

for name, grade, age in mylist2:
    if 'pat' in name:
        print(name, grade, age)

    if age is None:
        print(name, grade, age)



for index, row in df_census.iterrows():
    if row['race'].strip() == 'White':
        df_census.loc[index, 'is_white'] = True

print(df_census.tail(5).to_string())
print(df_census.columns)

for index, row in df_census.iterrows():
    if math.isnan(row['is_white']):
        print(row)


