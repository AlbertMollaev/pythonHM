import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
print(lst)

data = pd.DataFrame({'whoAmI':lst})

data.loc[data['whoAmI'] == 'robot', 'robot'] = '1'
data.loc[data['whoAmI'] == 'robot', 'human'] = '0'
data.loc[data['whoAmI'] == 'human', 'human'] = '1'
data.loc[data['whoAmI'] == 'human', 'robot'] = '0'

data = data.drop(columns=['whoAmI'])

# print(data.columns)
print(data.head(n = 20))