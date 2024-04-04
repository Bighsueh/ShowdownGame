from enum import Enum

class Suit(Enum):
    CLUBS = '1'
    DIAMONDS = '2'
    HEARTS = '3'
    SPADES = '4'

class Rank(Enum):
    TWO = ('2', 2)
    THREE = ('3', 3)
    FOUR = ('4', 4)
    FIVE = ('5', 5)
    SIX = ('6', 6)
    SEVEN = ('7', 7)
    EIGHT = ('8', 8)
    NINE = ('9', 9)
    TEN = ('10', 10)
    JACK = ('J', 11)
    QUEEN = ('Q', 12)
    KING = ('K', 13)
    ACE = ('A', 14)

class Card():
    def __init__(self, rank:Rank, suit: Suit) -> None:
        self.rank = rank
        self.suit = suit
        pass
    
    def value(self)->int:
        return int(self.suit.value) + int(self.rank.value)*4