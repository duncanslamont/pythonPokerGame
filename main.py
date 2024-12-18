import pygame
import random

hand = []
deck = []
table = []
for suit in ["spades","diamonds","hearts","clubs"]:
    for rank in ["ace","two","three","four","five","six","seven","eight","nine","ten","jack","queen","king"]:
        deck.append(rank + " of " + suit)

def deal(number_of_cards,location):
    dealt = random.sample(deck, number_of_cards)
    if location == "table":
        table.extend(dealt)
    else:
        hand.extend(dealt)
    for item in dealt:
        deck.remove(item)

def display():
    print("Table cards:")
    for card in table:
        print(card.ljust(30, "-"))
    print("Cards dealt to your hand:")
    for card in hand:
        print(card.ljust(30, "-"))

running = True
dealt = False
flop = False
turn = False
river = False

while running:
    if not dealt:
        deal(3,"table")
        deal(2,"hand")
        display()
        bet = int(input("Enter the amount you want to bet:"))
    print(bet)
    exit()
