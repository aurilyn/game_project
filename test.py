from game import *
from save import *

game = Game_Start()
try:
    load = Load()
    player_health, player_gold, player_inventory = load.load_save_to_game()
    player = Player(player_health, player_gold, player_inventory)
except:
    player = Player()
mob = Mobs()
combat = Combat()
saves = Save()
delete = Delete()
store = Store(player)

mob_attacks = mob.mob_attack()
# print(mob_attacks)

while player.player_health > 0:
    while player.player_health > 0 and mob.mob_health > 0:
        mob_attacks = mob.mob_attack()
        player_attack = input("Please select an attack ")
        player_damage, mob_damage = combat.combat(player_attack, mob_attacks)
        combat.damage_calc(player, mob, player_damage, mob_damage)
        print(f"You currently have {player.get_player_health()}HP")
        print(f"The opponent has {mob.get_mob_health()}HP")

    if player.player_health <= 0:
        break

    prompt = input(f"Shop or Continue? ")
    #once fight is over, ask user if they want to shop or continue to the next fight
    #after fight is over, prompt user
    if prompt == "Shop":
        item = store.display_store()
        store.buy_item(item)
        saves.update_save(player.get_player_health(), player.get_player_gold(), player.get_player_inventory())
    elif prompt == "Continue":
        mob = Mobs()