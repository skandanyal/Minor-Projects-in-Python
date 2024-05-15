from d16_coffee_maker import CoffeeMaker
from d16_menu import Menu, MenuItem
from d16_money_machine import MoneyMachine

# make objects from all the classes
coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()
options = menu.get_items()

# start the machine
is_on = True

while is_on:
    order = input(f"what would you like? ({options}): ").lower()

    if order == 'off':
        is_on = False

    elif order == 'report':
        coffee_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(order)
        # TODO: check sufficient resources
        if coffee_maker.is_resource_sufficient(drink):
            # todo: check if transaction successful
            if money_machine.make_payment(drink.cost):
                # todo: make the coffee
                coffee_maker.make_coffee(drink)






