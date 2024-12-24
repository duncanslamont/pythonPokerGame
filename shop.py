import sys
import random

money = 100
items = {"item1":[5,False],"item2":[6,False],"item3":[10,False]}
user_items = {}

def runShop():
    print("Items for sale:")
    i = 1
    running = True
    while running:
        for item in list(items.keys()):
            if item[1]:
                print(str(i) + ". " + item + ", costing " + str(items[item][0]))
            else:
                print(str(i) + ". " + item + ", costing " + str(items[item][0]) + " Sold!")
            i += 1
        number = int(input("Which item would you like to buy? Press 0 to buy no items."))
        if number == 0:
            print("No items bought.")
            return "Empty"
        elif number >= len(items.keys()):
            print("Not relevant number, try again.")
        else: 
            selected_item = list(items.keys())[number-1]
            if items[selected_item][0] > money:
                print("Not enough money, try again.")
            else:
                user_items[selected_item] = items[selected_item]
                items[selected_item][1] = True
                running = False
                
    print("Items:", items)
    print("User items:", user_items)

runShop()
# tes aasldkfjas dt
