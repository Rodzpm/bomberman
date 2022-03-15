import pygame 
from game import Game

def run():
  pygame.init()
  game = Game()
  game.run()


if "__main__" == __name__:
    run()