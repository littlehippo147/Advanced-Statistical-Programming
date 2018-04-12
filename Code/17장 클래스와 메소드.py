## printing objects

class Time(object):
    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))


start = Time()
start.hour = 9
start.minute = 45
start.second = 00
Time.print_time(start)
start.print_time()


## init method

class Time(object):
    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second


time = Time()
time.print_time()

time = Time(9)
time.print_time()

time = Time(9, 45)
time.print_time()


## str method

class Time(object):
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)


time = Time(9, 45)
print(time)


## operator overloading

class Time(object):
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def int_to_time(seconds):
        time = Time()
        minutes, time.second = divmod(seconds, 60)
        time.hour, time.minute = divmod(minutes, 60)
        return time

    def __add__(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)


start = Time(9, 45)
duration = Time(1, 35)
print(start + duration)


## type based dispatch

class Time(object):
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def int_to_time(seconds):
        time = Time()
        minutes, time.second = divmod(seconds, 60)
        time.hour, time.minute = divmod(minutes, 60)
        return time

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)


start = Time(9, 45)
duration = Time(1, 35)
print(start + duration)
print(start + 1337)
print(1337 + start)


## polymorphism

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] = d[c] + 1
    return d


t = ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam']
histogram(t)


## debugging
class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


p = Point(3, 4)
print(p.__dict__)


def print_attributes(obj):
    for attr in obj.__dict__:
        print(attr, getattr(obj, attr))


print_attributes(p)