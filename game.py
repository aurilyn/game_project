class Options:
    def __init__(self, deck, gold):
        self.deck = deck
        self.gold = gold

    def prompt(self):
        chamber = []
        limit = 5
        print(f"You have a limit of {limit} attacks you can make. Please select the order in which you want to send your attacks.")
        for i in range(limit):
            a = input(f"Please select attack {i+1}: ")
            chamber.append(a)
        print(chamber)

    def view_deck(self, deck):
        print(deck)

class Deck_Creation:
    def deck_init(self):
        deck = ["Rock", "Paper", "Scissors"]
        return deck