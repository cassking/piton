"""
Deal a hand of 5 cards
"""
import random
suits = ['♠︎', '♣︎', '♥︎', '♦︎']
values = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K']

cards = []  # fill list with cards
hand = []  # deal 5 random cards
# cannot get same card twice
cards2 = []
for suit in suits:
    for value in values:
        cards.append(suit + value)

for num in range(5):
    card = random.choice(cards)
    cards.remove(card) # to avoid dupes
    print(f"{card}")
    hand.append(card)

print(f"this  is the hand {hand}")
