import pygame
from piece import *

class Player:
    def __init__(self, color):
        self.color = color
        self.my_piece: list[PieceBase] = []
        self.__AddPiece()
        
    def __AddPiece(self):
        pawnY, otherY = (6, 7) if self.color == 'white' else (1, 0)

        for x in range(8):
            self.my_piece.append( Pawn(self.color, x, pawnY ))
            
        self.my_piece.append( Knight(self.color, 1, otherY ))
        self.my_piece.append( Knight(self.color, 6, otherY ))
        
        self.my_piece.append( Bishop(self.color, 2, otherY ))
        self.my_piece.append( Bishop(self.color, 5, otherY ))
        
        self.my_piece.append( Rook(self.color, 0, otherY ))
        self.my_piece.append( Rook(self.color, 7, otherY ))
        
        self.my_piece.append( Queen(self.color, 3, otherY ))
        self.my_piece.append( King(self.color, 4, otherY ))
        
    def draw(self, surface: pygame.Surface):
        for piece in self.my_piece:
            piece.draw(surface)
            
    def update(self, event):
        for piece in self.my_piece:
            piece.update(event)
            
    def getPiece(self, x, y):
        for piece in self.my_piece:
            if piece.x == x and self.y == y:
                return piece
        return None
    
    def totalValue(self):
        return sum(piece.value for piece in self.my_piece)
    