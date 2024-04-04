from player.Player import Player
from player.ComputerPlayer import ComputerPlayer
from player.RealPlayer import RealPlayer

from Deck import Deck
from Card import Card
from typing import List

class Game():
    def __init__(self) -> None:
        self.players: List[Player] = []
        self.turns: int
        self.deck: Deck
        self.board: List[tuple[Player,Card]] = []
        
        self.initTurns()
        self.initDeck()
    
    def initDeck(self) -> None:
        self.deck = Deck()
    
    def initTurns(self) -> None:
        self.turns = 1
        
    def addTurn(self,number)-> None:
        self.turns += number
    
    def setPlayer(self, playerType: str) -> None:       
        if playerType == 'pc':
            self.players.append(ComputerPlayer())       
        if playerType == 'real':
            self.players.append(RealPlayer())
        
    def gameStart(self)-> None:
        print("遊戲開始：")
        
        index = 1
        while True:
            # try:
            playerType = input(f"""新增玩家 {index},
欲新增真實玩家請輸入0, 欲新增電腦玩家請輸入1:""")

            if int(playerType) == 0:
                self.setPlayer('real')
            if int(playerType) == 1:
                self.setPlayer('pc')
            
            if len(self.players)>= 4:
                break
            else:
                index += 1
                
            # except:
            #     continue
            
        self.deck.initDeck()
        self.deck.shuffle()    
        pass
    
    def drawStage(self, players: List[Player])-> None:
        print('抽牌階段')
        while self.turns < 13:
            self.addTurn(1)
                
            for player in players:
                if player.hand.countCards() < 13:
                    card:Card = self.deck.drawCard()
                    player.hand.addCard(card = card)
                    
        for index, player in enumerate(players):
            handContent = [f'{card.suit.value[0]} {card.rank.value[0]},' for card in player.hand.cards]
            print(f'玩家{index+1} 手牌為 {handContent}')
        pass
    
    def takeTurn(self,player: Player, otherPlayers: List[Player])-> None:
        # 交換手牌
        if player.decideToExchange():
            player.chooseExchangePlayer(otherPlayers)
                
        # showCard
        card = player.hand.showCard()
        
        self.board.append(player,card)
        pass
    
    def mainStage(self, players: List[Player])-> None:       
        while self.turns < 13:
            print(f'第{self.turns}回合:')
            
            # 每個玩家輪流 takeTurn
            for index, player in enumerate(players):
                print(f'玩家{index+1} {player.name} 執行動作:')
                
                self.takeTurn(player = player,
                              otherPlayers= players[:index] + players[index + 1:])
                
                player.checkTurnCounter()
            
            # 顯示 players 出牌內容
            print('出牌結果')
            for item in self.board:
                player, card = item
                print(f'玩家: {player.name}, {card.suit}{card.rank}')
                
            # 比較手牌大小
            print('比較手牌大小')
            maxItem = tuple[Player,Card]
            maxScore:int = 0
            for item in self.board:
                player, card = item
                value = card.value()
                
                if maxScore < card.value() or maxScore == 0:
                    maxItem = item
                
            
            player,card = maxItem
            player.addPoint()
            
            print(f'本回合獲勝者: {player.name}, {card.suit}{card.rank}')
            self.turns += 1
                    
             
        #  13 回合後，P1~P4 皆已出完全部的牌，遊戲結束。取得最多分數的玩家為勝者，將勝者的名稱顯示出來。
        maxScore:int = 0
        winner:Player
        for player in players:
            if maxScore == 0 or maxScore < player.point:
                winner = player
        
        print(f'最終贏家：{winner.name}, 共{winner.point}點')
        pass
    
    def finish(self)-> None:
        print('遊戲結束')
    