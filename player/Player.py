from __future__ import annotations
from Hand import Hand
from Card import Card
from typing import List, Union

class Player:
    def __init__(self) -> None:
        self.point: int = 0
        self.order: int 
        self.name: str = 'nickname'
        self.hand: Hand = None
        self.exchangedTo: Player = None
        
        self.nameItSelf()
        self.setHand()
    def nameItSelf(self) -> None:
        pass
        
    def setHand(self)-> None:
        self.hand = Hand()
        
    def showCard(self) -> Card:
        pass
    
    def decideToExchange(self)->bool:
        pass
        
    def chooseExchangePlayer(self, players: List[Player]) -> None:
        pass
               
    def exchangeHand(self, player:Player) -> None:    
        # 交換兩個玩家的手牌
        player.hand, self.hand = self.hand, player.hand 
        
        # 紀錄跟誰換了手牌       
        self.exchangedTo = player 
        player.exchangedTo = self
    
    def exchangeBack(self)->None:
        self.hand.resetTurnCounter()
        self.exchangedTo.hand.resetTurnCounter()
        
        self.exchangeHand(self.exchangedTo)
        
    def checkTurnCounter(self)->None:
        self.hand.turnCounter -= 1
        
        if self.hand.turnCounter == 0:
            self.exchangeBack()
    
    def addPoint(self) -> int:
        self.point += 1
        return self.point
