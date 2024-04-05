from Card import Card
from typing import List

class Hand():    
    def __init__(self) -> None:
        self.cards: List[Card] = []
        self.turnCounter: int = 0
    
    def countCards(self) -> int:
        return len(self.cards)
    
    def addCard(self, card: Card) -> None:
        self.cards.append(card)

    def setTurnCounter(self) -> None:
        self.turnCounter = 3
        
    def resetTurnCounter(self) -> None:
        self.turnCounter = 0
        