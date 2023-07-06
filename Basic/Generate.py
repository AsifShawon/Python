import random
# from random import choice  # it means from random libraries we need choice function

# flipping a coin
# coin = random.choice(["Heads", "Tails"])  # [] is a list of 2 strings
# coin = choice(["Heads", "Tails"])
# print(coin)

#  generating random integer (randint) number from 1 to 10
# number = random.randint(1,10)
# print(number)

# shuffling
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)

