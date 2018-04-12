## updating variable

x = x + 1

x = 0
x = x + 1


## while statement

def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
    print('Blastoff!')


def sequence(n):
    while n != 1:
        print(n),
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1


# break

while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)

print('Done!')

# square root
epsilon = 1e-5
a = 2
x = 1

while True:
    print(x)
    y = (x + a / x) / 2
    if (abs(y - x) < epsilon):
        break
    x = y


