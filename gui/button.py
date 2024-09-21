import pygame_gui
import pygame

class StartButton:
    def hello_button(manager): 
        button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                                text='Start Game',
                                                manager=manager)
        return button