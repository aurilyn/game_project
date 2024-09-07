class Options:
    def prompt(self):
        chamber = []
        limit = 3
        print(f"You have a limit of {limit} attacks you can make. Please select the order in which you want to send your attacks.")
        for i in range(limit):
            a = input(f"Please select attack {i+1}: ")
            chamber.append(a)
        # print(chamber)
        return chamber

    def view_deck(self, deck):
        print(deck)

class Game_Start:
    def deck_init(self):
        deck = ["Rock", "Paper", "Scissors"]
        return deck
    
    def gold_init(self):
        gold = 15
        return gold
    
