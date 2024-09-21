import pygame

class StartingScreen:
    def main_screen():
        background = pygame.Surface((800, 600))
        background.fill(pygame.Color('#000000'))
        return background

class GameScreen:
    def second_screen():
        second_background = pygame.Surface((800, 600))
        second_background.fill(pygame.Color('#FF0000'))
        return second_background