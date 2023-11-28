import pygame
from player import Player

class PosMoveable:
    def __init__(self, color, x, y):
        self.pos_empty = []
        self.pos_rival = []
        
    def resetPos(self):
        self.pos_empty = []
        self.pos_rival = []
        
    def getPos(self, rivalPiece):
        ...