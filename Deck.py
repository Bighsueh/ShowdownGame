from Card import Card, Rank, Suit
from typing import List

import random

class Deck():
    def __init__(self) -> None:
        self.cards = List[Card]
    
    def shuffle(self) -> None:
        if not len(self.cards) > 0 : return None
        random.shuffle(self.cards)
    
    def initDeck(self) -> None:
        for suit in Suit:
            for rank in Rank:
                self.cards.append(Card( suit = suit, rank = rank))
        pass
    
    def drawCard(self) -> Card:
        return self.cards.pop() 