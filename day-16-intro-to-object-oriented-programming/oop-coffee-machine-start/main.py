from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine





OrderScreen = CoffeeMaker()
Till = MoneyMachine()
menu = Menu()

is_on = True

while is_on:
    response = input("What would you like? (espresso/latte/cappuccino): ")

    if any(response == x for x in ['espresso', 'latte', 'cappuccino']):
        drink = menu.find_drink(response)
        if OrderScreen.is_resource_sufficient(drink):
            if Till.make_payment(drink.cost):
                OrderScreen.make_coffee(drink)
            else:
                print("not enough money")
        else:
            print("Not enough ingredients")
    elif response == "report":
        OrderScreen.report()
        Till.report()
    elif response == "off":
        print("Have a nice day!")
        is_on = False
    else:
        print("not a valid option")