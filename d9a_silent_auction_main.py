'''
Author: Skandan C Y
Program: A Silent Bidding assist

This program takes in the names of various people who want to participate in a silent bid along with the amount of money that they wish to use and returns the name of the winner along with their bidding amount.
'''
import os
from d9b_silent_auction_art import logo

print(logo)


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


bidders = {}

def add_bidders(name, bid):
    bidders[name] = bid


def highest_bid(bidders):
    highest_bid = -999
    winner = ""
    for names in bidders:
        if bidders[name] > highest_bid:
            highest_bid = bidders[names]
            winner = names

    print(f'The winner is {winner} with a bid of rs.{highest_bid}')

is_bidding_over = False
while is_bidding_over == False:
    name = input('What is the name of the bidder? ')
    amount = int(input('What is your bid amount? rs.'))
    command = input('Is anyone else willing to bid? (yes/no)').lower()
    is_bidding_over = True if command != 'yes' else False
    add_bidders(name, amount)
    clear_console()

highest_bid(bidders)
