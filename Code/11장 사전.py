eng2sp =dict()
print(eng2sp)

eng2sp['one'] = 'uno'
print(eng2sp)

eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)
print(eng2sp['two'])

print(eng2sp['four'])

len(eng2sp)

'one' in eng2sp
'uno' in eng2sp

vals = eng2sp.values()
'uno' in vals


## a set of counters

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

h = histogram('brontosaurus')
print(h)


## looping

def print_hist(h):
    for c in h:
        print(c, h[c])

h = histogram('parrot')
print_hist(h)


## reverse lookup

def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise ValueError('value does not appear in the dictionary')

h = histogram('parrot')
k = reverse_lookup(h, 2)
print(k)
k = reverse_lookup(h, 3)


## dictionaries and lists

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


hist = histogram('parrot')
print(hist)
inverse = invert_dict(hist)
print(inverse)

t = [1, 2, 3]
d = dict()
d[t] = 'oops'


## memos

known = {0:0, 1:1}

def fibonacci(n):
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

fibonacci(3)

## global variables

verbose = True

def example1():
    if verbose:
        print('Running example 1')

example1()

been_called = False

def example2():  # wrong
    been_called = True

example2()
print(been_called)

def example2():  # correct
    global been_called
    been_called = True

example2()
print(been_called)

count = 0

def example3():
    global count
    count += 1

example3()
print(count)

known = {0:0, 1:1}

def example4():
    known[2] = 1

example4()
print(known)

def example5():
    global known
    known = dict()

example5()
print(known)
