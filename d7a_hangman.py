import random
from d7b_hangman_art import stages, logo, you_win, you_lose
from d7c_hangman_words import word_list

print(logo)

end_of_game = False
chosen_word = random.choice(word_list)
lives = 6
end_of_game = False

display = []
for _ in range(len(chosen_word)):
    display += '_'

while end_of_game == False:
    print(f'{''.join(display)}')
    guess = input("Guess the letter : ").lower()

    if guess in display:
        print(f'{guess} is already used')

    for letters in range(len(chosen_word)):
        if chosen_word[letters] == guess:
            display[letters] = chosen_word[letters]

    if guess not in chosen_word:
        lives -= 1
        print(f'{guess} is not in the word. you lose a life')
        if lives == 0:
            print(you_lose)
            end_of_game = True

    print(stages[lives])

    if '_' not in display:
        print(you_win)