from game import *
from save import *

game = Game_Start()
try:
    load = Load()
    player_health, player_gold = load.load_save_to_game()
    player = Player(player_health, player_gold)
except:
    player = Player()
mob = Mobs()
combat = Combat()
saves = Save()
delete = Delete()

# mob_attacks = mob.mob_attack()
# print(mob_attacks)

while player.player_health > 0 and mob.mob_health > 0:
    mob_attacks = mob.mob_attack()
    player_attack = input("Please select an attack ")
    player_damage, mob_damage = combat.combat(player_attack, mob_attacks)
    combat.damage_calc(player, mob, player_damage, mob_damage)
    print(f"You currently have {player.get_player_health()}HP")
    print(f"The opponent has {mob.get_mob_health()}HP")

saves.update_save(player.get_player_health(), player.get_player_gold())

