import pygame
import pygame_gui
import tkinter as tk
from tkinter import messagebox
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from game import Game_Start, Combat, Mobs, Player, Score

class StartingScreen:
    def main_screen():
        background = pygame.Surface((800, 600))
        background.fill(pygame.Color('#000000'))
        return background

class GameScreen:
    def __init__(self, manager):
        self.manager = manager
        self.game = Game_Start()
        self.combat = Combat()
        self.player = Player()
        self.mob = Mobs()
        self.score = Score()
        self.message_timer = 0
        self.player_score = 0

        screen_width, screen_height = 800, 600
        button_width, button_height = 100, 50
        button_x = screen_width - button_width - 10  # 10 pixels padding from the right edge

        self.rock_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((button_x, screen_height - 3 * button_height - 30), (button_width, button_height)),
            text='Rock',
            manager=self.manager
        )
        self.paper_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((button_x, screen_height - 2 * button_height - 20), (button_width, button_height)),
            text='Paper',
            manager=self.manager
        )
        self.scissors_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((button_x, screen_height - button_height - 10), (button_width, button_height)),
            text='Scissors',
            manager=self.manager
        )

        self.player_damage = 0
        self.mob_damage = 0

        try:
            self.player_image = pygame.image.load('sprite\player.png')
            self.player_image = pygame.transform.scale(self.player_image, (100, 100))
            self.player_image_rect = self.player_image.get_rect()
            self.player_image_rect.midbottom = (screen_width // 2, screen_height - 10)
        except pygame.error as e:
            print(f"Unable to load image: {e}")
            self.player_image = None

    def second_screen():
        second_background = pygame.Surface((800, 600))
        second_background.fill(pygame.Color('#FF0000'))
        return second_background
    
    def handle_events(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.rock_button:
                self.player_damage, self.mob_damage = self.combat.combat('Rock', self.game.mob.mob_attack())
                self.update()
            elif event.ui_element == self.paper_button:
                self.player_damage, self.mob_damage = self.combat.combat('Paper', self.game.mob.mob_attack())
                self.update()
            elif event.ui_element == self.scissors_button:
                self.player_damage, self.mob_damage = self.combat.combat('Scissors', self.game.mob.mob_attack())
                self.update()
                
    def update(self):
        self.game.player.update_player_health(self.game.player.get_player_health() - self.mob_damage)
        self.game.mob.update_mob_health(self.game.mob.get_mob_health() - self.player_damage)
        self.player_damage = 0
        self.mob_damage = 0

        if self.game.mob.get_mob_health() <= 0:
            self.player_score += self.score.point_calculation(self.game.player)
            root = tk.Tk()
            root.withdraw()
            continue_game = messagebox.askyesno("Continue to next mob?")
            root.destroy()

            self.continue_prompt = True

            if continue_game:
                self.game.mob = Mobs()
                self.score_calculated = False
                self.continue_prompt = False
            else:
                print("Gameover")
        
    def draw(self, surface=None):
        if surface is None:
            print("Surface is None, cannot draw.")
            return

        surface.fill((0, 0, 0))  # Clear the screen
        font = pygame.font.Font(None, 36)
        
        # Draw player health
        player_health_text = font.render(f"Player Health: {self.game.player.get_player_health()}", True, (255, 255, 255))
        player_health_text_rect = player_health_text.get_rect(center=(self.player_image_rect.centerx, self.player_image_rect.top - 20))
        surface.blit(player_health_text, player_health_text_rect)
        
        if self.player_image:
            surface.blit(self.player_image, self.player_image_rect)

        # Draw mob health
        mob_health_text = font.render(f"Mob Health: {self.game.mob.get_mob_health()}", True, (255, 255, 255))
        surface.blit(mob_health_text, (50, 100))

        if self.game.player.get_player_health() <= 0:
            game_over_text = font.render("You lost!", True, (255, 255, 255))
            score_text = font.render(f"Score: {str(self.player_score)}", True, (255, 255, 255))
            surface.blit(game_over_text, (50, 150))
            surface.blit(score_text, (50, 200))
        elif self.game.mob.get_mob_health() <= 0:
        # elif self.message_timer > 0:
            game_over_text = font.render("You won!", True, (255, 255, 255))
            surface.blit(game_over_text, (50, 150))
            if not self.score_calculated:
                score_text = font.render(f"Score: {str(self.player_score)}", True, (255, 255, 255))
                surface.blit(score_text, (50, 200))
                self.score_calculated = True