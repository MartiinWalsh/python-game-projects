from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

coffee_machine_is_on = True

while coffee_machine_is_on:
    options = menu.get_items()
    user_choice = input(f"What would you like? ({options}):")
    if user_choice == "off":
        coffee_machine_is_on = False
    elif user_choice == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_choice)
        if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(
            drink.cost
        ):
            coffee_machine.make_coffee(drink)
