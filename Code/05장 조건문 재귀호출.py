## modulus operator

quotient = 7/3
print(quotient)

remainder = 7 %3
print(remainder)


## Boolean expressions

5 == 5
5 == 6

type(True)
type(False)


## logical operators

17 and True


## conditional executtion
x = 1

if x > 0:
    print('x is positive')

if x < 0:
    pass        # does nothing

if x % 2 == 0:
    print('x is even')
else:
    print('x is odd')

y = 3

if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')

if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')


## recursion

def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

countdown(3)

def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)

print_n('Hello', 2)


## keyboard input

text = input()

print(text)

name = input('What is your name?\n')

print(name)

prompt = 'What is the velocity?\n'
speed = input(prompt)
int(speed)
