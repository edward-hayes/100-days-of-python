import sys

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money":0
}

def start():
    response = input("What would you like? (espresso/latte/cappuccino): ")

    def checkResources(drink):
        for ingredient in drink["ingredients"]:
            if drink[ingredient] > resources[ingredient]:
                print(ingredient)
    
    def directory(response):
        if any(response == x for x in ['espresso', 'latte', 'cappuccino']):
            print("you want a",response)
            checkResources(MENU[response])
        elif response == "report":
            print("Water: " + str(resources["water"]) + "ml")
            print("Milk: " + str(resources["milk"]) + "ml")
            print("Coffee: " + str(resources["coffee"]) + "g")
            print("Money: $" + "{:.2f}".format(resources["money"]))
        elif response == "off":
            print("Have a nice day!")
            quit()
        else:
            print("not a valid option")
     
    directory(response)

while(True):
    start()