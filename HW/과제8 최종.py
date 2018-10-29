# inside class Point :

class Point(object):
    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)

    def __add__(self, other):
        add = Point()
        if type(other) == tuple:
            add.x = self.x + other[0]
            add.y = self.y + other[1]
            return add
        elif type(other) == Point:
            add.x = self.x + other.x
            add.y = self.y + other.y
            return add

type(tu)
tu = (2,1)
point = Point()
point.x = 6
point.y = 7

point.__str__()

print(point)

other = Point()
other.x = 4
other.y = -2

print(point + other)
add = Point()
add.x = point.x + other.x
add.y = point.y + other.y
print(add.x, add.y)

print(point + tu)

import random

class Card(object):
    """Represents a standard playing card."""

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __gt__(self, other):
        # check the suits
        if self.suit > other.suit:
            return True
        elif self.suit < other.suit:
            return False
        else:
            if self.rank > other.rank:
                return True
            return False

    def cmp(self, other):
        return (self > other) - (other > self)


class Deck(object):

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def sort(self):
        self.cards.sort()

    def deal_hands(self, num_hands, cards_perhand):
        if (num_hands * cards_perhand) <= 52:
            hands = []
            for num in range(num_hands):
                hand = Hand()
                for card in range(cards_perhand):
                    hand.add_card(self.pop_card())
                hands.append(hand)
            return hands
        else:
            print('패가 너무 많아 카드가 부족합니다.')

deck = Deck()
print(deck)
deck.shuffle()
deck.sort()

class Hand(Deck):
    def __init__(self, label=''):
        self.cards = []
        self.label = label



deck = Deck()
deck.shuffle()
print(deck)

deck.deal_hands(4, 15)
hand = deck.deal_hands(4, 6)
print(hand[0])
print(hand[2])





import sys

sys.path.append("/full/path/to/folder/containing/matplotlib.py")

import sys
import os
import pkg_resources
from pprint import pprint


pprint({
    'sys.version_info': sys.version_info,
    'sys.prefix': sys.prefix,
    'sys.path': sys.path,
    'pkg_resources.working_set': list(pkg_resources.working_set),
    'PATH': os.environ['PATH'].split(os.pathsep),
})

import matplotlib
import tensorflow

## matplotlib

from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

plt.title("Nominal GDP")

plt.ylabel("Billions of $")

plt.show()

## bar chart

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

xs = [i + 0.1 for i, _ in enumerate(movies)]  # place the bar at center

plt.bar(xs, num_oscars)
plt.ylabel("# of Academy Awards")
plt.title("My Favoriate Movies")

plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)  # movie titles
plt.show()

## histogram

from collections import Counter

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
decile = lambda grade: grade // 10 * 10
histogram = Counter(decile(grade) for grade in grades)

plt.bar([x - 4 for x in histogram.keys()],  # shift each bar to the left by 4
        histogram.values(),  # give each bar its correct height
        8)  # give each bar a width of 8
plt.axis([-5, 105, 0, 5])  # x-axis from -5 to 105,
# y-axis from 0 to 5
plt.xticks([10 * i for i in range(11)])  # x-axis labels at 0, 10, ..., 100
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")
plt.show()

## line chart

variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)]

xs = range(len(variance))

# we can make multiple calls to plt.plot
# to show multiple series on the same chart
plt.plot(xs, variance, 'g-', label='variance')  # green solid line
plt.plot(xs, bias_squared, 'r-.', label='bias^2')  # red dot-dashed line
plt.plot(xs, total_error, 'b:', label='total error')  # blue dotted line

# because we've assigned labels to each series
# we can get a legend for free
# loc=9 means "top center"
plt.legend(loc=9)
plt.xlabel("model complexity")
plt.title("The Bias-Variance Tradeoff")
plt.show()

## scatterplot

friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes)

# label each point
for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label,
                 xy=(friend_count, minute_count),  # put the label with its point
                 xytext=(5, -5),  # but slightly offset
                 textcoords='offset points')

plt.title("Daily Minutes vs. Number of Friends")
plt.xlabel("# of friends")
plt.ylabel("daily minutes spent on the site")
plt.show()

# axes are not comparable

test_1_grades = [99, 90, 85, 97, 80]
test_2_grades = [100, 85, 60, 90, 70]

plt.scatter(test_1_grades, test_2_grades)
plt.title("Axes Aren't Comparable")
plt.xlabel("test 1 grade")
plt.ylabel("test 2 grade")
plt.show()

# axes are comparable

plt.scatter(test_1_grades, test_2_grades)
plt.title("Axes Are Comparable")
plt.axis("equal")
plt.xlabel("test 1 grade")
plt.ylabel("test 2 grade")
plt.show()

import tensorflow as tf
import numpy as np

tf.set_random_seed(777)
print(tf.__version__)

x_data = np.array([[0, 0],
                  [0, 1],
                  [1, 0],
                  [1, 1]], dtype=np.float32)
y_data = np.array([[0],
                  [0],
                  [0],
                  [1]], dtype=np.float32)

X = tf.placeholder(tf.float32, [None, 2], name='x-input')
Y = tf.placeholder(tf.float32, [None, 1], name='y-input')

W = tf.Variable(tf.random_normal([2, 1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

hypothesis = tf.sigmoid(tf.matmul(X, W) + b)

cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1 - Y) * tf.log(1 - hypothesis))
train = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)

predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32))

with tf.Session() as sess:
    # Initialize TensorFlow variables
    sess.run(tf.global_variables_initializer())

    for step in range(10001):
        sess.run(train, feed_dict={X: x_data, Y: y_data})

        if step % 100 == 0:
            print(step, sess.run(cost, feed_dict={X: x_data, Y: y_data}), sess.run(W))

    # Accuracy report
    h, c, a = sess.run([hypothesis, predicted, accuracy], feed_dict={X: x_data, Y: y_data})
    print("\nHypothesis: ", h, "\nCorrect: ", c, "\nAccuracy: ", a)
