from d13b_upper_or_lower_data import data
from d13c_upper_or_lower_art import logo
from d13c_upper_or_lower_art import vs
from random import randint

print(logo)


def answer(follower_1, follower_2, choice):
    """
    function to determine if the answer given by the user is correct or not
    :param follower_1: follower count of card 1
    :param follower_2: follower count of card 2
    :param choice: answer given by the user
    :return: True / False
    """
    if follower_1 > follower_2:
        if choice.lower() == 'a':
            return True
        else:
            return False

    elif follower_2 > follower_1:
        if choice.lower() == 'b':
            return True
        else:
            return False


def selection_of_card(card_1, score):
    """
    select cards for each iteration
    :param card_1: first card
    :param score : current score of the game
    :return: two cards to play the game with
    """
    # unpack card 1
    card_1 = card_1

    # card 0
    card_0 = 0

    # pick the second card
    while (card_2 := randint(0, 49)) == card_1:
        while (card_2 := randint(0, 49)) == card_0:
            pass

    # display their info
    print("Choose between: ")
    print(f"A: {data[card_1]['name']}, a {data[card_1]['description']}, from {data[card_1]['country']}")
    print(vs)
    print(f"B: {data[card_2]['name']}, a {data[card_2]['description']}, from {data[card_2]['country']}")

    # take input from the user
    while (choice := input("type 'A' or 'B': ").lower()) not in ['a', 'b']:
        pass

    print("\n\n")

    # check if the input is correct
    follower_1 = data[card_1]['follower_count']
    follower_2 = data[card_2]['follower_count']

    # if user answered correctly
    if answer(follower_1, follower_2, choice):
        card_0 = card_1
        card_1 = card_2

        # print the current score
        print(f"Current score = {score + 1}")

        # recurse the loop
        selection_of_card(card_2, score + 1)

    # if user did not answer correctly
    else:
        print(f"Final score = {score}")
        return True,


if __name__ == "__main__":
    player_lost = False
    while player_lost == False:
        _ = input("Press enter to continue")
        score = 0
        card_1 = randint(0, 49)
        player_lost = selection_of_card(card_1, score)
        print("Click Run to play once again")
