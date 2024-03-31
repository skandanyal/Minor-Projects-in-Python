rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random


def game(user, computer, user_score, computer_score):

    if user == computer:
        print("It is a tie")
        print(f"score:\nuser = {user_score}\ncomputer = {computer_score}")

    elif (user == 1 and computer == 2) or (user == 2 and computer == 3) or (user == 3 and computer == 1):
        print("Computer wins this round")
        computer_score += 1
        print(f"score:\nuser = {user_score}\ncomputer = {computer_score}")

    else:
        print("User wins this round")
        user_score += 1
        print(f"score:\nuser = {user_score}\ncomputer = {computer_score}")

    return user_score, computer_score


def inputs(user_score, computer_score):
    user = int(input("Enter 1 for 'rock', 2 for 'paper' and 3 for 'scissors': "))
    computer = random.randint(1, 3)

    if user not in [1, 2, 3]:
        print("Enter a valid input")
        inputs(user_score, computer_score)

    if user == 1:
        print('user: ', rock)
    elif user == 2:
        print('user: ', paper)
    else:
        print('user: ', scissors)

    if computer == 1:
        print('computer: ', rock)
    elif computer == 2:
        print('computer: ', paper)
    else:
        print('computer: ', scissors)

    user_score, computer_score = game(user, computer, user_score, computer_score)

    return user_score, computer_score


def best_of(number_of_turns):
    user_score = 0
    computer_score = 0

    for turns in range(number_of_turns):
        print(f"Turn {turns + 1} out of {number_of_turns}:")
        user_score, computer_score = inputs(user_score, computer_score)

    return user_score, computer_score


print("Rock, Paper, Scissors")
number_of_turns = int(input("Enter the number of times you want to play the game: "))
if number_of_turns % 2 == 0:
    print("Invalid input. Restart the game.")

user_score, computer_score = best_of(number_of_turns)

print(f"At the end of the game,\nuser has scored {user_score} points\ncomputer has scored {computer_score} points")
if user_score == computer_score:
    print("It is a tie")
elif user_score > computer_score:
    print("User wins!")
else:
    print("Computer wins!")