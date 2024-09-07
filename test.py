from game import *
import time

game = Game_Start()
player = Player()
mob = Mobs()
combat = Combat()

mob_attacks = mob.mob_attack()
print(mob_attacks)
player_attacks = []
player_attack_limit = 3
#allow the player to select their attacks
time.sleep(5)
while len(player_attacks) < player_attack_limit:
    player_input = input("Please select which attack you want to use: ")
    #verify if the input is the right type
    if player_input not in ["Rock", "Paper", "Scissors"]:
        player_input = input("Please try again.")
    else:
        player_attacks.append(player_input)
        print(f"You have {player_attack_limit - len(player_attacks)} attacks left")

#after player selects their attacks, go to combat
player_damage, mob_damage = combat.combat(player_attacks, mob_attacks)

new_player_health, new_mob_health = combat.damage_calc(player_damage, mob_damage)
player.update_player_health(new_player_health)
mob.update_mob_health(new_mob_health)

print(f"Player Health: {player.get_player_health()}")
print(f"Mob Health: {mob.mob_health}")