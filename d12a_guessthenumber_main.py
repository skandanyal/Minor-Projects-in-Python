from random import randint
from d12b_guessthenumber_art import logo

print(logo)

def prompts(number, hardness):
    if hardness == 'easy':
        n = 0
        while n < 10:
            guess = int(input("Enter the guess: "))

            if guess == number:
                print("You have guessed it correctly!")
                exit(0)

            if -5 < (guess - number) < 5:
                print("You're very close")

            elif -15 < (guess - number) < 15:
                print("You're close, but not too close")

            elif -25 < (guess - number) < 25:
                print("You're far, but not too far")

            elif -35 < (guess - number) < 35:
                print("You're kinda far")

            elif -45 < (guess - number) < 45:
                print("You're very far")

            elif -55 < (guess - number) < 55:
                print("SO farrr away")

            elif -100 < (guess - number) < 100:
                print("ded ded ded you're soo ded")

            print(f"You have {9-n} turns left")

            n += 1

        print(f"The number to guess was {number}")
        print("Your turns are over.")
        exit(0)

    elif hardness == 'medium':
        n = 0
        while n < 6:
            guess = int(input("Enter the guess: "))

            if guess == number:
                print("You have guessed it correctly!")
                exit(0)

            if -5 < (guess - number) < 5:
                print("You're very close")

            elif -15 < (guess - number) < 15:
                print("You're close, but not too close")

            elif -25 < (guess - number) < 25:
                print("You're far, but not too far")

            elif -35 < (guess - number) < 35:
                print("You're kinda far")

            elif -45 < (guess - number) < 45:
                print("You're very far")

            elif -55 < (guess - number) < 55:
                print("SO farrr away")

            elif -100 < (guess - number) < 100:
                print("ded ded ded you're soo ded")

            print(f"You have {5-n} turns left")

            n += 1

        print(f"The number to guess was {number}")
        print("Your turns are over.")
        exit(0)

    elif hardness == 'hard':
        n = 0
        while n < 3:
            guess = int(input("Enter the guess: "))

            if guess == number:
                print("You have guessed it correctly!")
                exit(0)

            if -5 < (guess - number) < 5:
                print("You're very close")

            elif -15 < (guess - number) < 15:
                print("You're close, but not too close")

            elif -25 < (guess - number) < 25:
                print("You're far, but not too far")

            elif -35 < (guess - number) < 35:
                print("You're kinda far")

            elif -45 < (guess - number) < 45:
                print("You're very far")

            elif -55 < (guess - number) < 55:
                print("SO farrr away")

            elif -100 < (guess - number) < 100:
                print("ded ded ded you're soo ded")

            print(f"You have {2-n} turns left")

            n += 1

        print(f"The number to guess was {number}")
        print("Your turns are over.")
        exit(0)




number = randint(1, 100)
hardness = input("Enter preferred hardness level from 'Easy', 'Medium'. 'Hard': ").lower()

prompts(number, hardness)
