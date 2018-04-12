#import os
#os.chdir("c:/temp")
#os.getcwd()

## Reading and writing

fout = open('output.txt', 'w')
print(fout)

line1 = "This here's the wattle,\n"
fout.write(line1)

line2 = "the emblem of our land.\n"
fout.write(line2)

fout.close()



## format operator

camels = 42
'%d' % camels
'I have spotted %d camels.' % camels

'In %d years I have spotted %g %s.' % (3, 0.1, 'camels')

'%d %d %d' % (1,2)
'%d' % 'dollars'



## filenames and paths

import os
cwd = os.getcwd()
print(cwd)

os.path.exists('output.txt')
os.path.isdir('output.txt')
os.listdir(cwd)

def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            print path
        else:
            walk(path)



## catching exceptions

try:
    fin = fopen('bad_file')
    for line in fin:
        print(line)
    fin.close()
except:
    print('Something went wrong.')


## pickling

import pickle
t = [1, 2, 3]
s = pickle.dumps(t)
print(s)
t2 = pickle.loads(s)
print(t2)
t == t2
t is t2


## writing modules
# wc.py
def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count

import wc

print(wc)
wc.linecount('wc.py')


## delimiated file

# tab delimited
import csv

def process(date, symbol, price):
    print(date, symbol, price)

with open('D:/Dropbox/�곗씠�� 諛깆뾽/Lecture/2018�� 1�숆린 怨좉툒�듦퀎�꾨줈洹몃옒諛�/肄붾뱶/tab_delimited_stock_prices.txt', 'r', encoding='utf8',newline='') as f:
    reader = csv.reader(f, delimiter='\t')
    # reader = csv.reader(codecs.iterdecode(f, 'utf-8'), delimiter='\t')
    for row in reader:
        date = row[0]
        symbol = row[1]
        closing_price = float(row[2])
        process(date, symbol, closing_price)

# colon delimited
with open('D:/Dropbox/�곗씠�� 諛깆뾽/Lecture/2018�� 1�숆린 怨좉툒�듦퀎�꾨줈洹몃옒諛�/肄붾뱶/colon_delimited_stock_prices.txt', 'r', encoding='utf8',newline='') as f:
    reader = csv.DictReader(f, delimiter=':')
    # reader = csv.DictReader(codecs.iterdecode(f, 'utf-8'), delimiter=':')
    for row in reader:
        date = row["date"]
        symbol = row["symbol"]
        closing_price = float(row["closing_price"])
        process(date, symbol, closing_price)

# csv.writer
today_prices = { 'AAPL' : 90.91, 'MSFT' : 41.68, 'FB' : 64.5 }

with open('D:/Dropbox/�곗씠�� 諛깆뾽/Lecture/2018�� 1�숆린 怨좉툒�듦퀎�꾨줈洹몃옒諛�/肄붾뱶/comma_delimited_stock_prices.txt','w', encoding='utf8',newline='') as f:
    writer = csv.writer(f, delimiter=',')
    for stock, price in today_prices.items():
        writer.writerow([stock, price])


## debugging

s = '1 2\t 3\n 4'
print(s)

print(repr(s))