import pygame 
from board import Board
from player import Player

class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = Player('white')
        self.player2 = Player('black')
        
    def update(event):
        ...
        
    def draw(self, surface: pygame.display):
        self.board.draw(surface)
        self.player1.draw(surface)
        self.player2.draw(surface)