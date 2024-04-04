from Hand import Hand
from player.Player import Player
from typing import List, Union

class RealPlayer(Player):
    def __init__(self) -> None:
        super().__init__()
        
    def nameItSelf(self) -> None:
        self.name = str(input('請輸入姓名:'))
    
    def setHand(self) -> None:
        super().setHand()
    
    def decideToExchange(self)->bool:
        if not self.exchangedTo == None: return False # 已經交換過，取消交易
        
        print('請問執行動作“指定玩家並與其交換手牌”嗎？')
        while True:
            try:
                return bool(input('請輸入True或False:'))
            except:
                continue
    
    def chooseExchangePlayer(self, players: List[Player]) -> None:       
        print('可交換玩家列表：')
        for index, otherPlayer in enumerate(players):
            if otherPlayer.exchangedTo == None:
                print(f'{index+1}: {otherPlayer.name}')
        
        targetIndex = int(input('請輸入想要交換牌組的對象'))
        choosenPlayer = players[targetIndex]
        if not targetIndex == 0 : 
            print(f'選擇與{choosenPlayer.name} 交換')
            self.exchangeHand(choosenPlayer)     
            
            # 設定三回合倒數換牌
            self.hand.setTurnCounter()
            choosenPlayer.hand.setTurnCounter()  
    
    def exchangeHand(self, player: Player) -> None:
        super().exchangeHand(player)
    
    def exchangeBack(self)->None:
        super().exchangeBack()
        
    def checkTurnCounter(self) -> None:
        return super().checkTurnCounter()
    
    def addPoint(self) -> int:
        return super().addPoint()