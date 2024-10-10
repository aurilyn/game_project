import pygame_gui
import pygame

class StartButton:
    def hello_button(manager): 
        button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                                text='Start Game',
                                                manager=manager)
        return button
    
    def rock_button(manager):
        button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 400), (100, 50)),
                                                text='Rock',
                                                manager=manager)
        return button
    
    def paper_button(manager):
        button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 400), (100, 50)),
                                                text='Paper',
                                                manager=manager)
        return button
    
    def scissor_button(manager):
        button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 400), (100, 50)),
                                                text='Scissors',
                                                manager=manager)
        return button