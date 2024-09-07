import random
import numpy as np

# class Options:
#     def __init__(self):
#         self.player_health = 15

#     def prompt(self):
#         chamber = []
#         limit = 3
#         print(f"You have a limit of {limit} attacks you can make. Please select the order in which you want to send your attacks.")
#         for i in range(limit):
#             a = input(f"Please select attack {i+1}: ")
#             chamber.append(a)
#         # print(chamber)
#         return chamber
    
#     def get_player_health(self):
#         return self.player_health
    
#     def update_player_health(self, new_health):
#         self.player_health = new_health

#     def view_deck(self, deck):
#         print(deck)

class Game_Start:
    def __init__(self):
        self.player = Player()
        self.mob = Mobs()

class Player:
    def __init__(self) -> None:
        self.player_health = 15
        self.player_armour = 0
        self.player_gold = 10
        self.player_deck = ["Rock", "Paper", "Scissors"]
    
    def get_player_health(self):
        return self.player_health
    
    def update_player_health(self, new_health):
        self.player_health = new_health
        
class Mobs:
    def __init__(self) -> None:
        self.mob_health = 15
        self.mob_armour = 0
        self.attacks = ["Rock", "Paper", "Scissors"]

    def mob_attack(self):
        mob_attack = np.random.choice(self.attacks, 3)
        return mob_attack

    def update_mob_health(self, new_health):
        self.mob_health = new_health

class Combat:
    def __init__(self):
        self.winning_conditions = {
            "Rock": "Scissors",
            "Paper": "Rock",
            "Scissors": "Paper"
        }

    def damage(self, player_attack, mob_attack):
        if player_attack == mob_attack:
            return 0
        elif self.winning_conditions[player_attack] == mob_attack:
            return 1
        else:
            return -1
            
    def combat(self, player_attacks, mob_attacks):
        mob_damage = 0
        player_damage = 0

        for player_attack, mob_attack in zip(mob_attacks, player_attacks):
            result = self.damage(player_attack, mob_attack)
            if result == 1:
                player_damage += 1
            elif result == -1:
                mob_damage += 1
            else:
                pass
        return mob_damage, player_damage
    
    def damage_calc(self, player_damage, mob_damage):
        mobs = Mobs()
        player = Player()

        player.player_health -= mob_damage
        mobs.mob_health -= player_damage    
        return player.player_health, mobs.mob_health