## return values

# area of a circle
def area(radius):
    temp = math.pi * radius ** 2
    return temp


def area(radius):
    return math.pi * radius ** 2


# multiple return

def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x


# wrong
def absolute_value(x):
    if x < 0:
        return -x
    if x > 0:
        return x


print(absolute_value(0))


## incremental development

# example
# step 1
def distance(x1, y1, x2, y2):
    return 0.0


# test
distance(1, 2, 4, 6)


# step 2
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    print('dx is', dx)
    print('dy is', dy)
    return 0.0


# test
distance(1, 2, 4, 6)


# step 3
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx ** 2 + dy ** 2
    print('dsquared is', dsquared)
    return 0.0


# test
distance(1, 2, 4, 6)

# step 4
import math


def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx ** 2 + dy ** 2
    result = math.sqrt(dsquared)
    return result


# test
distance(1, 2, 4, 6)


## composition
def circle_area(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return result


# more concisely
def circle_area(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))


## boolean functions

def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False


is_divisible(6, 4)

is_divisible(6, 3)


# more cosisely
def is_divisible(x, y):
    return x % y == 0


# unconditional statement
if is_divisible(x, y):
    print('x is divisible by y')

# equivelently
if is_divisible(x, y) == True:
    print('x is divisible by y')


## more reccusions

def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n - 1)
        result = n * recurse
        return result


# checking types

def factorial(n):
    if not isinstance(n, int):
        print('Factorial is only defined for integers.')
        return None
    elif n < 0:
        print('Factorial is not defined for negative integers.')
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)


factorial('fred')
factorial(-2)


## debugging
def factorial(n):
    space = ' ' * (4 * n)
    print(space, 'factorial', n)
    if n == 0:
        print(space, 'returning 1')
        return 1
    else:
        recurse = factorial(n - 1)
        result = n * recurse
        print(space, 'returning', result)
        return result


factorial(4)