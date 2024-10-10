import pygame
import pygame_gui
from game import Game_Start, Combat, Mobs, Player

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

        self.rock_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((50, 400), (100, 50)),
            text='Rock',
            manager=self.manager
        )
        self.paper_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((200, 400), (100, 50)),
            text='Paper',
            manager=self.manager
        )
        self.scissors_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((350, 400), (100, 50)),
            text='Scissors',
            manager=self.manager
        )

        self.player_damage = 0
        self.mob_damage = 0

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
        
    def draw(self, surface=None):
        surface.fill((0, 0, 0))  # Clear the screen
        font = pygame.font.Font(None, 36)
        
        # Draw player health
        player_health_text = font.render(f"Player Health: {self.game.player.get_player_health()}", True, (255, 255, 255))
        surface.blit(player_health_text, (50, 50))
        
        # Draw mob health
        mob_health_text = font.render(f"Mob Health: {self.game.mob.get_mob_health()}", True, (255, 255, 255))
        surface.blit(mob_health_text, (50, 100))

        if self.game.player.get_player_health() <= 0:
            game_over_text = font.render("You lost!", True, (255, 255, 255))
            surface.blit(game_over_text, (50, 150))
        elif self.game.mob.get_mob_health() <= 0:
            game_over_text = font.render("You won!", True, (255, 255, 255))
            surface.blit(game_over_text, (50, 150))