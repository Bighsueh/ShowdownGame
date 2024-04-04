from Card import Card
from Card import Rank
from Card import Suit
from typing import List

import random

class Deck():
    def __init__(self) -> None:
        self.cards: List[Card] = []
    
    def shuffle(self) -> None:
        random.shuffle(self.cards)
    
    def initDeck(self) -> None:
        for suit in Suit:
            for rank in Rank:
                self.cards.append(Card( suit = suit, rank = rank))
        self.shuffle()
    
    def drawCard(self) -> Card:
        return self.cards.pop() 