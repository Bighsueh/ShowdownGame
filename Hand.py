from Card import Card
from typing import List

class Hand():    
    def __init__(self) -> None:
        self.cards: List[Card] = []
        self.turnCounter: int = 0
    
    def showCard(self) -> Card:
        print('當前手牌如下: ')
        for index, card in enumerate(self.cards):
            print(f'{index} => {card.suit}{card.rank}')
        
        cardIndex = int(input('請輸入欲出牌的編號: '))
        
        card = self.cards[cardIndex]
        self.cards.remove(card)
        
        return card

    def addCard(self, card: Card) -> None:
        self.cards.append(card)

    def setTurnCounter(self, int) -> None:
        self.turnCounter = 3
        
    def resetTurnCounter(self) -> None:
        self.turnCounter = 0
        