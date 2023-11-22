import pygame
from const import *
from game import Game

class Main:
    def __init__ (self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Chess')
        LOGO = pygame.image.load('assets/images/white_king.png').convert_alpha()
        pygame.display.set_icon(LOGO)
        
        self.game = Game()
        self.running = True
        
    def mainLoop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            
            self.game.draw(self.screen)
            pygame.display.update()
        pygame.quit()
        sys.exit()
    
main = Main()
main.mainLoop()