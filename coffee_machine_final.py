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
}


def check_resources(drink_ingredients):
    """
    function to check if enough resources are available to prepare the coffee
    param req_ingredients: ingredients required to prepare the order
    :return: True if yes, False if no
    """
    for item in resources:
        if drink_ingredients[item] > resources[item]:
            print(f"Sorry there's not enough {item}. Order something else please!")
            return False
    return True


def check_transaction(drink_cost):
    """
    function to check if the customer has paid enough or not
    :param profit: total amount of cash collected till now
    :return: True if customer pays complete money, False if customer does not pay complete money
    """
    print("Use coins please:")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01

    if total >= drink_cost:
        print(f"Here is ${(total - drink_cost):.2f} in change. ")
        global profit
        profit += drink_cost
        return True

    else:
        print("Sorry that's not enough money. Money refunded. ")
        return False


def prepare_coffee(drink, order):
    """
    function to update the resources and serve the coffee
    :param order: order placed
    :param drink: order placed, tracked to the dictionary
    :return: None
    """
    for item in resources:
        resources[item] -= drink['ingredients'][item]
    print(f"Here is your {order}. Enjoy!")


profit = 0
is_on = True

while is_on == True:
    order = input(">>What would you like to have? (espresso/latte/cappuccino): ").lower()

    # print report
    if order == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    # turn off
    elif order == 'off':
        exit(0)

    # make coffee
    else:
        drink = MENU[order]
        if check_resources(drink['ingredients']):
            if check_transaction(drink['cost']):
                prepare_coffee(drink, order)
