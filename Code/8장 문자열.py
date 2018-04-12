## string is a sequence

fruit = 'banana'
letter = fruit[1]
print(letter)

letter = fruit[0]
print(letter)

letter = fruit[1.5]

len(fruit)

length = len(fruit)
last = fruit[length]
print(last)

print(fruit[-1])

fruit[0:5:2]    # step size 2
fruit[::-1]     # backward

# escape sequence

sentence = "He said, \"This parrot's dead.\""
sentence
print(sentence)
subjects = 'Physics\nChemistry\nBiology'
subjects
print(subjects)



## traversal

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

# equivalently

for char in fruit:
    print(char)


prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    print(letter + suffix)


## slicing

s = 'Monty Python'
print(s[0:5])
print(s[6:12])
fruit[:3]
fruit[3:]
fruit[3:3]


## print function

heading = '| Index of Dutch Tuplip Prices |'
line = '+' + '-'*16 + '-'*14 + '+'
print(line, heading, line,
      '|     Nov 23 1636 |        100 |',
      '|     Nov 25 1636 |        673 |', line, sep='\n')



## immutability

greeting = 'Hello, world!'
greeting[0] = 'J'

new_greeting = 'J' + greeting[1:]
print(new_greeting)


## searching

def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

find(fruit, 'n')

## counting

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)


## string methods
word = 'banana'
new_word = word.upper()
print(new_word)

word.find('na')
word.find('na', 3)

name = 'bob'
name.find('b', 1, 2)


a = 'java python c++ fortran'
a.isalpha()
b = a.title()
b
c = b.replace(' ', '!\n')
c
print(c)
c.index('Python')



## in operator

'a' in 'banana'
'seed' in 'banana'

def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)

in_both('apples', 'oranges')



## string comparison
word = 'apple'

if word == 'banana':
    print('All right, bananas.')

if word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bananas.')


## debugging

def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False

    i = 0
    j = len(word2)

    while j > 0:
        print(i, j)
        if word1[i] != word2[j]:
            return False
        i = i + 1
        j = j - 1

    return True

is_reverse('pots', 'stop')


def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False

    i = 0
    j = len(word2) - 1

    while j > 0:
        print(i, j)
        if word1[i] != word2[j]:
            return False
        i = i + 1
        j = j - 1

    return True

is_reverse('pots', 'stop')

