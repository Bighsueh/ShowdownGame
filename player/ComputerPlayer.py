from Hand import Hand
from player.Player import Player
from typing import List, Union
import random

class ComputerPlayer(Player):
    def __init__(self) -> None:
        super().__init__()
        
    def nameItSelf(self) -> None:
        self.name = "pc"
               
    def setHand(self) -> None:
        super().setHand()
    
    def decideToExchange(self)->bool:
        if not self.exchangedTo == None: return None # 已經交換過，取消交易
        
        return random.choice([True, False])# 隨機選擇要不要交換
    
    def chooseExchangePlayer(self, players: List[Player]) -> None:
        while True:
            # 隨機選個交換玩家
            exchangePlayer:Player = random.choice(players)
            
            # 若玩家已經執行/被執行過交換則退出
            if not exchangePlayer.exchangedTo == None: return None
        
            # 玩家尚未執行/被執行過交換, 則開始交換
            print(f'選擇與 {exchangePlayer.name} 交換')
            self.exchangeHand(exchangePlayer)
            
            # 設定三回合倒數換牌
            self.hand.setTurnCounter()
            exchangePlayer.hand.setTurnCounter()
    
    def exchangeHand(self, player: Player) -> None:
        return super().exchangeHand(player)
    
    def exchangeBack(self)->None:
        super().exchangeBack()
        
    def checkTurnCounter(self) -> None:
        return super().checkTurnCounter()
    
    def addPoint(self) -> int:
        return super().addPoint()