import pygame
from const import *

class Board:
    def __init__(self):
        ...

    def draw(self, surface: pygame.Surface):
        self.__drawBoard(surface)
        self.__drawNumberLetter(surface)
           
    def __drawBoard(self, surface: pygame.Surface):
        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    color = BOARD_LIGHT
                else:
                    color = BOARD_DARK
                rect = pygame.Rect(col*SQSIZE, row*SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(surface, color, rect)
    
    def __drawNumberLetter(self, surface: pygame.Surface):
        # draw 1->8, A->H
        for i in range(8):
            if i % 2 == 0:
                color = BOARD_LIGHT
            else:
                color = BOARD_DARK
            number = font_small.render(str(i+1), True, color)
            number_rect = number.get_rect(topright=(8*SQSIZE-2, i*SQSIZE-2))
            surface.blit(number, number_rect)
            
            letter = font_small.render(chr(i+65), True, color)
            letter_rect = letter.get_rect(bottomleft=(i*SQSIZE+2, 8*SQSIZE+2))
            surface.blit(letter, letter_rect)