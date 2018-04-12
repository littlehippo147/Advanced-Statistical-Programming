## tuples are immutable

t = 'a', 'b', 'c', 'd', 'e'
# or
t = ('a', 'b', 'c', 'd', 'e')

# tuple with a single element
t1 = 'a',
type(t1)

t2 = ('a')
type(t2)

t = tuple()
print(t)

t = tuple('lupins')
print(t)
print(t[0])
print(t[1:3])


mylist = [1,2]
mytuple = (1,2)
othertuple = 3, 4
mylist[1] = 3

try:
    mytuple[1] = 3
except TypeError:
    print("cannot modify a tuple")


# immutable
t[0] = 'A'

# replacing is fine
t = ('A',) + t[1:]
print(t)



## assignment

addr = 'monty@python.org'
uname, domain = addr.split('@')

print(uname)
print(domain)


## as return values

t = divmod(7,3)
print(t)

quot, rem = divmod(7,3)
print(quot)
print(rem)

def min_max(t):
    return min(t), max(t)

def sum_and_product(x, y):
    return (x+y), (x*y)

sp = sum_and_product(2,3)
print(sp)
s, p = sum_and_product(5,10)
print(s, p)




## variable-length arguments tuple

def printall(*args):
    print(args)

printall(1, 2.0, '3')

t = (7, 3)
divmod(t)
divmod(*t)


## lists and tuples

t=[('a',0), ('b',1), ('c',2)]

for letter, number in t:
    print(number, letter)

for index, element in enumerate('abc'):
    print(index, element)


## dictionaries and tuples

d = {'a':0, 'b':1, 'c':2}
t = d.items()
print(t)

dict_items([('a', 0), ('b', 1), ('c', 2)])
d = dict(t)
print(d)

for key,val in d.items():
    print(val, key)


directory = dict()
directory['Cleese','John'] = '08700 100 222'
directory['Chapman', 'Graham'] = '08700 100 222'
for last,first in directory:
    print(first, last, directory[last,first])


## Comparing tuples

(0,1,2) < (0,3,4)
(0,1,2000000) < (0,3,4)


def sort_by_length(words):
    t = []
    for word in words:
        t.append((len(word), word))

    t.sort(reverse=True)

    res = []
    for length, word in t:
        res.append(word)
    return res

wdlist = ['dumb', 'apple', 'cliche']
sort_by_length(wdlist)


## other examples

t = (1, 'two', 3.)
t
t[1]
t[2] = 4

t = (1, ['a', 'b', 'c'], 0)
t[1][2] = 'c'
t

a = [1, 2, 3]
b = ['a', 'b', 'c']

z = zip(a,b) # zip

for pair in z:
    print(pair)

list(zip(a,b))
