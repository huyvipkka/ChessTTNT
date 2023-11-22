import pygame
from const import *


class PieceBase:            
    def __init__(self, path2img: str, color: str, x: int, y: int, value: int):
        self.image = pygame.image.load(path2img).convert_alpha()
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.color = color
        self.value = value
        
    def update(self, event):
        ...
    
    def draw(self, surface: pygame.Surface):
        centerX = self.x*SQSIZE + SQSIZE // 2
        centerY = self.y*SQSIZE + SQSIZE // 2
        self.rect.center = (centerX, centerY)
        surface.blit(self.image, self.rect)
        
class Pawn(PieceBase):
    def __init__(self, color, x, y):
        path = f'assets/images/{color}_pawn.png'
        PieceBase.__init__(self, path, color, x, y, 1)
        
class Knight(PieceBase):
    def __init__(self, color, x, y):
        path = f'assets/images/{color}_knight.png'
        PieceBase.__init__(self, path, color, x, y, 3)
        
class Bishop(PieceBase):
    def __init__(self, color, x, y):
        path = f'assets/images/{color}_bishop.png'
        PieceBase.__init__(self, path, color, x, y, 4)
        
class Rook(PieceBase):
    def __init__(self, color, x, y):
        path = f'assets/images/{color}_rook.png'
        PieceBase.__init__(self, path, color, x, y, 5)
        
class Queen(PieceBase):
    def __init__(self, color, x, y):
        path = f'assets/images/{color}_queen.png'
        PieceBase.__init__(self, path, color, x, y, 9)

class King(PieceBase):
    def __init__(self, color, x, y):
        path = f'assets/images/{color}_king.png'
        PieceBase.__init__(self, path, color, x, y, 10000)

