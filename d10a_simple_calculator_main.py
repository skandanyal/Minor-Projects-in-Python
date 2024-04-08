from d10b_simple_calculator_art import logo
import os


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1/n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculator():
    print(logo)
    num1 = float(input("Enter the first number: \n"))

    calculation = True

    while calculation:
        operation = input(
            "'+'\n'-'\n'*'\n'/'\nPick an operation from the line above: \n")
        if operation not in operations:
            print("Enter a valid input: \n")
            continue
        num2 = float(input("Enter the next number: \n"))

        calc_function = operations[operation]
        answer = calc_function(num1, num2)

        print(f'{num1:.4f} {operation} {num2:.4f} = {answer:.4f}')

        choice = input(
            "Press 'y' to continue calculation with the previous answer and 'n' to start calculation all over again.\n")
        if choice.lower() == 'y':
            num1 = answer
        else:
            calculation = False
            '''clears the console'''
            os.system('cls' if os.name == 'nt' else 'clear')
            calculator()



calculator()