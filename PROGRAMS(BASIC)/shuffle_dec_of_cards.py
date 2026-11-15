
import random

suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
ranks = ["A", "2", "3", "4", "5", "6", "7",
         "8", "9", "10", "J", "Q", "K"]

deck = []

for suit in suits:
    for rank in ranks:
        deck.append(rank + " of " + suit)

random.shuffle(deck)

for card in deck:
    print(card)
