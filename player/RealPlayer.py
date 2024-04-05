from Hand import Hand
from Card import Card
from player.Player import Player
from typing import List, Union

class RealPlayer(Player):
    def __init__(self) -> None:
        super().__init__()
        
    def nameItSelf(self) -> None:
        self.name = str(input('請輸入姓名:'))
    
    def setHand(self) -> None:
        super().setHand()
        
    def showCard(self) -> Card:
        print('當前手牌如下: ')
        for index, card in enumerate(self.hand.cards):
            print(f'{index} => {card.suit.value[0]}{card.rank.value[0]}')
        
        cardIndex = int(input('請輸入欲出牌的編號: '))
        
        card = self.hand.cards[cardIndex]
        self.hand.cards.remove(card)
        
        return card
    
    def decideToExchange(self)->bool:
        if not self.exchangedTo == None: return False # 已經交換過，取消交易
        
        print('請問執行動作“指定玩家並與其交換手牌”嗎？')
        while True:
            try:
                exchange:str = input(f"""欲交換則輸入 1, 不交換則輸入0""")
                return  int(exchange) == 1
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