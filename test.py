from game import *

game_init = Game_Start()
opt = Options()
deck = game_init.deck_init()
# print(game_init.deck_init(), game_init.gold_init())

opt.prompt()