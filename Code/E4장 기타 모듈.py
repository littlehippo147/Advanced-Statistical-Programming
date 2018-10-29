# Summary/DImensions/Structure
import pandas as pd

data = pd.read_csv('d:/ext5handling/titanic3.csv')

data.head()
data.shape
data.columns.values
data.describe()
data.dtypes

# Handling missing Values
pd.isnull(data['body'])
pd.notnull(data['body'])
pd.isnull(data['body']).values.ravel().sum()
pd.notnull(data['body']).values.ravel().sum()

# data.dropna(axis=0,how='all')
# data.dropna(axis=0,how='any')
# data.fillna(0)
# data.fillna('missing')
# data['body'].fillna(0)
# data['body']
# data['age']
# data['age'].fillna(data['age'].mean())
# data['age'].fillna(method='ffill')
# data['age'].fillna(method='backfill')


# Dummy Variable

dummy_sex = pd.get_dummies(data['sex'], prefix='sex')
column_name = data.columns.values.tolist()
column_name.remove('sex')
data[column_name].join(dummy_sex)

# Selecting  column(s)
import pandas as pd

data = pd.read_csv('d:/ext5handling/Customer Churn Model.txt')
account_length = data['Account Length']
account_length.head()

subdata = data[['Account Length', 'VMail Message', 'Day Calls']]
subdata.head()

# Selecting/Ignoring particular columns
wanted_columns = ['Account Length', 'VMail Message', 'Day Calls']
subdata = data[wanted_columns]
subdata.head()

wanted = ['Account Length', 'VMail Message', 'Day Calls']
column_list = data.columns.values.tolist()
sublist = [x for x in column_list if x not in wanted]
subdata = data[sublist]
subdata.head()

# Selecting rows with row numbers and conditional filters
data[1:50]
data[25:75]
data[:50]
data[51:]

# Creating new columns
data['Total Mins'] = data['Day Mins'] + data['Eve Mins'] + data['Night Mins']
data['Total Mins'].head()

data1 = data[data['Total Mins'] > 500]
data1.shape

data1 = data[data['State'] == 'VA']
data1.shape

data1 = data[(data['Total Mins'] > 500) & (data['State'] == 'VA')]
data1.shape

data1 = data[(data['Total Mins'] > 500) | (data['State'] == 'VA')]
data1.shape

# Selecting combination of rows and columns
subdata_first_50 = data[['Account Length', 'VMail Message', 'Day Calls']][1:50]
subdata_first_50

data.ix[1:100, 1:6]
data.ix[:, 1:6]
data.ix[1:100, :]
data.ix[1:100, [2, 5, 7]]
data.ix[[1, 2, 5], [2, 5, 7]]
data.ix[[1, 2, 5], ['Area Code', 'VMail Plan', 'Day Mins']]

# Generating a dummy data frame to illustrate groupby method

import numpy as np
import pandas as pd
import random

a = ['Male', 'Female']
b = ['Rich', 'Poor', 'Middle Class']
gender = []
seb = []

for i in range(1, 101):
    gender.append(np.random.choice(a))
    seb.append(np.random.choice(b))

height = 30 * np.random.randn(100) + 155
weight = 20 * np.random.randn(100) + 60
age = 10 * np.random.randn(100) + 35
income = 1500 * np.random.randn(100) + 15000

df = pd.DataFrame(
    {'Gender': gender, 'Height': height, 'Weight': weight, 'Age': age, 'Income': income, 'Socio-Eco': seb})
df.head()

# Print group names and groups

grouped = df.groupby('Gender')
for names, groups in grouped:
    print(names)
    print(groups)

grouped = df.groupby(['Gender', 'Socio-Eco'])
for names, groups in grouped:
    print(names)
    print(groups)

# Aggregation

grouped = df.groupby(['Gender', 'Socio-Eco'])
grouped.sum()
grouped.size()
grouped.describe()

grouped.aggregate({'Income': np.sum, 'Age': np.mean, 'Height': np.std})
grouped.aggregate({'Age': np.mean, 'Height': lambda x: np.mean(x) / np.std(x)})
grouped.aggregate([np.sum, np.mean, np.std])

# Filtering

grouped['Age'].filter(lambda x: x.sum() > 700)

# Transformation

zscore = lambda x: (x - x.mean()) / x.std()
grouped.transform(zscore)

f = lambda x: x.fillna(x.mean())
grouped.transform(f)

# Concatenating Datasets

import pandas as pd

data1 = pd.read_csv('d:/ext5handling/winequality-red.csv', sep=';')
data1.head()

data2 = pd.read_csv('d:/ext5handling/winequality-white.csv', sep=';')
data2.head()

wine_total = pd.concat([data1, data2], axis=0)
wine_total.head

filepath = 'd:/ext5handling'
data_final = pd.read_csv('d:/ext5handling/001.csv')
data_final_size = len(data_final)
for i in range(1, 333):
    if i < 10:
        filename = '0' + '0' + str(i) + '.csv'
    if 10 <= i < 100:
        filename = '0' + str(i) + '.csv'
    if i >= 100:
        filename = str(i) + '.csv'
    file = filepath + '/' + filename
    data = pd.read_csv(file)
    data_final_size += len(data)
    data_final = pd.concat([data_final, data], axis=0)

data_final.tail()
print(data_final_size)

# Merging/Joining Datasets

import pandas as pd

data_main = pd.read_csv('d:/ext5handling/Medals.csv')
data_main.head()

a = data_main['Athlete'].unique().tolist()
len(a)

country_map = pd.read_csv('d:/ext5handling/Athelete_Country_Map.csv')
country_map.head()

sports_map = pd.read_csv('d:/ext5handling/Athelete_Sports_Map.csv')
sports_map.head()

sports_map[(sports_map['Athlete'] == 'Chen Jing') | (sports_map['Athlete'] == 'Richard Thompson') | (
            sports_map['Athlete'] == 'Matt Ryan')]

merged = pd.merge(left=data_main, right=country_map, left_on='Athlete', right_on='Athlete')
merged.head()

country_map_dp = country_map.drop_duplicates(subset='Athlete')

merged_dp = pd.merge(left=data_main, right=country_map_dp, left_on='Athlete', right_on='Athlete')
len(merged_dp)

sports_map_dp = sports_map.drop_duplicates(subset='Athlete')
len(sports_map_dp)

merged_final = pd.merge(left=merged_dp, right=sports_map_dp, left_on='Athlete', right_on='Athlete')
merged_final.head()