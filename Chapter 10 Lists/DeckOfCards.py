'''
Card numbers 0 to 12, 13 to 25, 26 to 38, and 39 to 51 represent
13 spades, 13 hearts, 13 diamonds, and 13 clubs, respectively
=>cardNumber // 13 determines the suit of the card and
cardNumber % 13 determines the rank of the card
'''
import random
deck = [x for x in range(52)]
#create suits and ranks list
suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
ranks = ["ace","1","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]

random.shuffle(deck)

for i in range(4):
    suit = suits[deck[i] // 13]
    rank = ranks[deck[i] % 13]
    print("Card number", deck[i], "is the", rank, "of", suit)
