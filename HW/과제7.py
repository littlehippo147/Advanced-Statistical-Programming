import math
class Point(object):
    """Represents a point in 2-D space."""

def distance_between_points(point1, point2):
    dis_x = point1.x - point2.x
    dis_y = point1.y - point2.y
    distance = math.sqrt(dis_x ** 2 + dis_y ** 2)
    return distance

p1 = Point()
p2 = Point()

p1.x = 5.0; p1.y = 16.0; p2.x = 10.0; p2.y = 4.0

distance_between_points(p1, p2)

class Rectangle(object):
    """Represents a rectangle.

    attributes: width, height, corner.
    """

box = Rectangle()
box.width = 50.0
box.height = 100.0
box.corner = Point()
box.corner.x = 50.0
box.corner.y = 0.0


def move_rectangle(rectangle, dx, dy):
    rectangle.corner.x += dx
    rectangle.corner.y += dy

move_rectangle(box, 30, 20)

def print_point(p):
    print('(%g, %g)' % (p.x, p.y))
print_point(box.corner)

import copy

def move_rectangle_copy(rectangle, dx, dy):
    new = copy.deepcopy(rectangle)
    new.corner.x += dx
    new.corner.y += dy
    print_point(new.corner)
    return(new)


move_rectangle_copy(box, -30, -20)

print_point(new.corner)


class Time(object):
    """Represents the time of day.

    attributes: hour, minute, second
    """

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True

def print_time(time):
    print('%g hour %g minutes %g seconds' % (time.hour, time.minute, time.second))

def mul_time(time, num):
    assert valid_time(time)
    newtime = int_to_time(num * time_to_int(time))
    return  print_time(newtime)

time = Time()
time.hour = 2
time.minute = 10
time.second = 30

mul_time(time, 3)


def avr_pace(runtime, mile):
    return mul_time(runtime, 1 / mile)

runtime = Time()
runtime.hour = 4
runtime.minute = 20
runtime.second = 40
avr_pace(runtime, 4)

today()

from datetime import datetime

def today_weekday():
    today = datetime.today()
    print(today)
    print(today.strftime('%A'))

today_weekday()

def until_birthday():
    try:
        print('When is your date of birth?')
        year = int(input("year > "))
        month = int(input("month > "))
        day = int(input("day > "))

        today = datetime.today()
        birthday = datetime(today.year, month, day)
        if today > birthday:
            birthday = datetime(today.year + 1, month, day)

        print('Until your birthday..')
        print(birthday - today)
    except:
        print('날짜가 잘못 입력되었습니다. 다시 입력해주세요')

until_birthday()

