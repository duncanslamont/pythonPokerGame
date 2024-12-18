import sys
import random


items = {"item1":5,"item2":6,"item3":10}

def runShop():
    print("Items for sale:")
    i = 1
    for item in list(items.keys()):
        print(str(i) + ". " + item + ", costing " + str(items[item]))
        i += 1

    number = input("Which item would you like to buy? Press 0 to buy no items.")
runShop()
