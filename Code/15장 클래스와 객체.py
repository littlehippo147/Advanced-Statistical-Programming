## user-defined types

class Point(object):
    """Represents a point in 2-D space."""

print(Point)
blank = Point()
print(blank)


## attributes
blank.x = 3.0
blank.y = 4.0
print(blank.x)
print(blank.y)
print('(%g, %g)' % (blank.x, blank.y))
distance = math.sqrt(blank.x**2 + blank.y**2)
print(distance)

def print_point(p):
    print('(%g, %g)' % (p.x, p.y))

print_point(blank)


## rectangles

class Rectangle(object):
    """Represents a rectangle.

    attributes: width, height, corner.
    """

box = Rectangle()
box.width = 100
box.height = 200
box.corner = Point()
box.corner.x = 0
box.corner.y = 0


## instances as return values

def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p

center = find_center(box)
print_point(center)


## objects are mutable

def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight

print(box.width)
print(box.height)
print_point(box.corner)
grow_rectangle(box, 50, 100)
print(box.width)
print(box.height)
print_point(box.corner)


## copying

p1 = Point()
p1.x = 3
p1.y = 4

import copy
p2 = copy.copy(p1)

print_point(p1)
print_point(p2)
p1 is p2
p1 == p2

box2 = copy.copy(box)
box2 is box
box2.corner is box.corner

box3 = copy.deepcopy(box)
box3 is box
box3.corner is box.corner


## debugging

p = Point()
p.x = 0
p.y = 0
print(p.z)

type(p)

hasattr(p, 'x')
hasattr(p, 'z')





