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