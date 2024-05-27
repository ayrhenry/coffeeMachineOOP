from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



menu = Menu()
cm = CoffeeMaker()
mm = MoneyMachine()

vending = True;

while vending:

    userInput = input("What would you like? (espresso/latte/cappuccino/)")

    if userInput == "off":
        vending = False
    elif(userInput == "report"):
        cm.report()
        mm.report()
    else:
        userInput = menu.find_drink(userInput)
        if cm.is_resource_sufficient(userInput):
            if mm.make_payment(userInput.cost):
                cm.make_coffee(userInput)
        
            

