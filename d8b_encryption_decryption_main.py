'''
Author: Skandan.C.Y
Program: Caeser cipher
Description: *The following program takes in three inputs - the text to be operated upon, the operation to be performed(encryption/decryption)
and the key of the operation.
*The program gives out the text after performing the operation as preferred by the user
'''
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from d8a_encryption_decryption_art import logo

def caeser(text, shift, dirn):
    new_word = ""
    for letters in text:
        if letters in alphabet:
            new_index = (alphabet.index(letters) + (shift * dirn)) % 26
            new_word += alphabet[new_index]
        else:
            new_word += letters

    return new_word


print(logo)
word = input("Enter the text: ")
direction = input("What action would you like to perform: encryption or decryption?  ").lower()
if direction == "encryption" or direction == "encrypt":
    dirn = 1
elif direction == "decryption" or direction == "decryption":
    dirn = -1
else:
    print("Input error: restart the program")
shift = int(input("Enter the shift value/key: "))

new_word = caeser(word, shift, dirn)

print(f"The {direction}ed word is {new_word}")