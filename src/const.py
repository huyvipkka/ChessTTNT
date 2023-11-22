import pygame

pygame.init()

WIDTH = HEIGHT = 600
SQSIZE = WIDTH / 8

BOARD_DARK = (167, 113, 31, 255)
BOARD_LIGHT = (255, 251, 161, 255)

font_small = pygame.font.SysFont('arial', int(SQSIZE/3), True)