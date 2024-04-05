from Game import Game
from player.Player import Player


game = Game()

game.initTurns()
game.gameStart()
game.drawStage(game.players)
game.mainStage(game.players)
game.finish()
    