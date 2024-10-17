import pygame
import pygame_gui
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from gui.screens import *
from gui.button import *

pygame.init()
pygame.display.set_caption('Rock Paper Scissors')
pygame_icon = pygame.image.load('sprite\player.png')
pygame.display.set_icon(pygame_icon)

window_surface = pygame.display.set_mode((800, 600))

manager = pygame_gui.UIManager((800,600), theme_path="gui/theme.json")

start_button = StartButton.hello_button(manager)

clock = pygame.time.Clock()
is_running = True

current_view = 'main'
game_screen = None

while is_running:     
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == start_button:
                current_view = 'game'
                start_button.kill()
                game_screen = GameScreen(manager)

        manager.process_events(event)

        if current_view == 'game':
            game_screen.handle_events(event)

    if current_view == 'main':
        window_surface.blit(StartingScreen.main_screen(), (0, 0))
        manager.update(time_delta)
        manager.draw_ui(window_surface)
    elif current_view == 'game':
        window_surface.blit(GameScreen.second_screen(), (0, 0))
        game_screen.update() #update game state
        game_screen.draw(window_surface)
        manager.update(time_delta)
        manager.draw_ui(window_surface)
    pygame.display.update()