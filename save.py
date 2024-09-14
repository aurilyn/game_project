import json
import os

class Save:
    def __init__(self) -> None:
        self.save = {
            "player_health": 15,
            "player_gold": 15,
            "player_inventory": []
        }

    def update_save(self, player_health, player_gold, player_inventory):
        self.save["player_health"] = player_health
        self.save["player_gold"] = player_gold
        self.save["player_inventory"] = player_inventory

        with open("save.json", "w") as f:
            json.dump(self.save, f)
class Load:
    def __init__(self) -> None:
        with open("save.json", "r") as f:
            self.data = json.load(f)
    
    def load_save_to_game(self):
        player_health = self.data["player_health"]
        player_gold = self.data["player_gold"]
        player_inventory = self.data["player_inventory"]
        return player_health, player_gold, player_inventory
    
class Delete:
    def delete_save(self):
        delete = False
        prompt = input("Would you like to delete your save? ")
        if prompt == "Yes":
            delete = True
        if delete == True:
            os.remove("save.json")
        