##### 1번

import random

from matplotlib import pyplot as plt


random.seed(147)
x = range(1000)

unif = []

for i in x:
    unif.append(random.uniform(0,1))

y = []

def mean(x):
    return sum(x) / len(x)

for i in x:
    y.append(mean(unif[0:i+1]))

plt.plot(x, y, color = 'black', linestyle = 'solid')
plt.title("Mean of Uniform dist")

y[999]


##### 2번

import random

def number_game():
    number = random.randint(1, 100)
    while True:
        what_number = int(input("1 부터 100, 맞춰보세요 "))
        if what_number < 1 or what_number > 100:
            print('정신 차리세요.')
        elif what_number > number:
            print('좀 더 낮춰도 될 것 같아요.')
        elif what_number < number:
            print('그것보단 클 것 같아요.')
        else:
            print('정답입니다! 오래 걸리셨네요ㅎ')
            break

number_game()


##### 3번
import matplotlib
import pandas as pd

medal = pd.read_csv('d:/ext5handling/Medals.csv')
country = pd.read_csv('d:/ext5handling/Athelete_Country_Map.csv')
sports = pd.read_csv('d:/ext5handling/Athelete_Sports_Map.csv')

medal.head()
country.head()

Main_data = pd.merge(left = medal, right = country, left_on = 'Athlete', right_on = 'Athlete')
Main_data.head()

need_col = ['Athlete', 'Year', 'Gold Medals', 'Silver Medals', 'Bronze Medals', 'Total Medals', 'Country']
Korea = Main_data[need_col][Main_data['Country'] == 'South Korea']
Korea.head()

Korea_year = Korea.groupby('Year')
year_res = Korea_year.sum()
year_res

Korea_athl = Korea.groupby('Athlete')
athl_res = Korea_athl.sum()
athl_sort = athl_res.sort_values(by = ['Gold Medals', 'Silver Medals', 'Bronze Medals'], axis = 0, ascending=False)
athl_sort