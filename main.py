import pandas as pd
import pprint

crime_df = pd.read_csv('/Users/edwardcarron/DataSets/Police/cally_all_cats_data.csv')
data = crime_df.to_dict()
data

ready_data = []

for cat, dict in data.items():
    ready_datas = {'data': []}
    for nums in dict.values():
        ready_datas['data'].append(nums)
    ready_data.append(ready_datas)


pprint.pprint(ready_data)











