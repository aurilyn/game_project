import numpy as np
import random

class Game_Start:
    def __init__(self):
        self.player = Player()
        self.mob = Mobs()

class Player:
    def __init__(self, player_health=15, player_gold=15, player_inventory=None):
        self.player_health = player_health
        self.player_armour = 0
        self.player_gold = player_gold
        self.player_inventory = player_inventory if player_inventory else []
        self.player_deck = ["Rock", "Paper", "Scissors"]
    
    def get_player_health(self):
        return self.player_health
    
    def get_player_gold(self):
        return self.player_gold
    
    def update_player_health(self, new_health):
        # print(new_health)
        self.player_health = new_health
        
    def get_player_inventory(self):
        return self.player_inventory
    
    def update_player_inventory(self, new_item):
        self.player_inventory.append(new_item)

    def select_attack(self, attack):
        print(attack)
    
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
    def __init__(self, player):
        self.player = player
        self.store = {
            "item_1": "C",
            "item_2": "C",
            "item_3": "C",
            "item_4": "UC",
            "item_5": "UC",
            "item_5": "R"
        }
        self.price = {
            "C": 5,
            "UC": 10,
            "R": 15
        }
        
    def display_store(self):
        store = random.sample(list(self.store), 3)
        for item in store:
            rarity = self.store[item]
            price = self.price[rarity]
            output = f"{item}: {price}g"
            print(output)

        while True:
            selected_item = input("Type in the item you would like to buy: ")
            if selected_item not in store:
                print("Item not in store")
            else:
                return selected_item
    
    def buy_item(self, item):
        rarity = self.store[item]
        price = self.price[rarity]
        if self.player.player_gold >= price:
            self.player.player_gold -= price
            inventory = self.player.get_player_inventory()
            inventory.append(item)
            print(self.player.player_inventory)
            print(self.player.player_gold)
        else:
            print("Insufficient Funds")