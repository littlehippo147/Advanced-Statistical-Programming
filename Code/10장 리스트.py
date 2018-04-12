## list

[10, 20, 30, 40]
['crunchy frog', 'ram bladder', 'lark vomit']
['spam', 2.0, 5, [10, 20]]
cheeses = ['Cheddar', 'Edam', 'Gouda']
numbers = [17, 123]
empty = []
print(cheeses, numbers, empty)

## mutable

print(cheeses[0])
numbers = [17, 123]
numbers[1] = 5
print(numbers)

'Edam' in cheeses
'Brie' in cheeses


## traversing

for cheese in cheeses:
    print(cheese)

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

for x in []:
    print('This never happens.')

x = ['spam', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
x[3]



## operation

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

[0] * 4
[1, 2, 3] * 3


## slicing

t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1:3]
t[:4]
t[3:]
t[:]

t[1:3] = ['x', 'y']
print(t)


## methods

t = ['a', 'b', 'c']
t.append('d')
print(t)

t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
print(t1)

t2.insert(3, 'f')
print(t2)

t = ['a', 'b', 'c']
t.remove('b')
print(t)
t.index('a')

t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print(t)
t.reverse()
t


## map, filter and reduce

def add_all(t):
    total = 0
    for x in t:
        total += x
    return total


t = [1, 2, 3]
sum(t)


def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res


def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res


## deleting elements

t = ['a', 'b', 'c']
x = t.pop(1)
print(t)
print(x)


t = ['a', 'b', 'c']
del t[1]
print(t)


t = ['a', 'b', 'c']
x = t.remove('b')
print(t)


t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]
print(t)


## lists and strings

s = 'spam'
t = list(s)
print(t)


s = 'printing for the fjords'
t = s.split()
print(t)


s = 'spam-spam-spam'
delimiter = '-'
s.split(delimiter)


t = ['pining', 'for', 'the', 'fjords']
delimiter = ' '
delimiter.join(t)


## objects and values

a = 'banana'
b = 'banana'
a is b

a = [1, 2, 3]
b = [1, 2, 3]
a is b



## aliasing

a = [1, 2, 3]
b = a
b is a

b[0] = 17
print(a)


## list arguments

def delete_head(t):
    del t[0]


letters = ['a', 'b', 'c']
delete_head(letters)
print(letters)

t1 = [1, 2]
t2 = t1.append(3)
print(t1)
print(t2)

t3 = t1 + [4]
print(t3)

def bad_delete_head(t):
    t = t[1:]

def tail(t):
    return t[1:]

letters = ['a', 'b', 'c']
rest = tail(letters)
print(rest)



## examples

x = range(10)
print(x[0])
print(x[1])
print(x[-1])
print(x[-2])

print(x[:3])
print(x[3:])
print(x[1:5])
print(x[-3:])
print(x[1:-1])

1 in [1,2,3]
0 in [1,2,3]

x = [1,2,3]
x.extend([4,5,6])
print(x)

x = [1,2,3]
y = x + [4,5,6]
print(x, y)

x.append(0)
print(x)

