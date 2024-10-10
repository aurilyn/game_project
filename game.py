import numpy as np
import json

class Game_Start:
    def __init__(self):
        self.player = Player()
        self.mob = Mobs()

class Player:
    def __init__(self, player_health=3, player_gold=10):
        self.player_health = player_health
        self.player_armour = 0
        self.player_gold = player_gold
        self.player_deck = ["Rock", "Paper", "Scissors"]
    
    def get_player_health(self):
        return self.player_health
    
    def get_player_gold(self):
        return self.player_gold
    
    def update_player_health(self, new_health):
        print(new_health)
        self.player_health = new_health
        
class Mobs:
    def __init__(self) -> None:
        self.mob_health = 3
        self.mob_armour = 0
        self.attacks = ["Rock", "Paper", "Scissors"]

    def mob_attack(self):
        mob_attack = np.random.choice(self.attacks, 1)
        return mob_attack
    
    def get_mob_health(self):
        return self.mob_health

    def update_mob_health(self, new_health):
        print(new_health)
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

        # for player_attack, mob_attack in zip(mob_attacks, player_attacks):
        result = self.damage(player_attacks, mob_attacks)
        if result == 1:
            player_damage += 1
        elif result == -1:
            mob_damage += 1
        else:
            pass
        return player_damage, mob_damage
    
    def damage_calc(self, player, mobs, player_damage, mob_damage):
        player.player_health -= mob_damage
        mobs.mob_health -= player_damage

        player.update_player_health(player.player_health)
        mobs.update_mob_health(mobs.mob_health)
        # return player.player_health, mobs.mob_health

class Store:
    def __init__(self, items):
        #items is a dictionary of items with the item name as key and cost is the value
        self.items = items
        self.store_item_limit = 6
    def items(self):
        #load in the items that can be purchased
        store_items = []
        items = store_items.append(np.random.choice(self.items, self.store_item_limit))
        return items
    def display_items(self, items):
        for item in items:
            print(f"{item}, Price: 6 Gold")
    def purchase(self):
        

