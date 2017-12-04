# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of
# lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new
# password every time the user asks for a new password. Include your code in a main method.
#
# Extra:
#
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
import string
import random


def ask_user():
    user_input = input('Do you want a random password to be generated? y/n: ')
    if user_input.lower() == 'y':
        user_choice = input('Do you want a hard or an easy password? Enter "h" for hard and "e" for easy: ')
        if user_choice == 'h':
            print('Here is your hard password: ' + str(generate_random_hard_password()))
        elif user_choice == 'e':
            print('Here is your easy password: ' + str(generate_random_easy_password()))
        else:
            print('Invalid input')
    else:
        print('Bye')


def generate_random_hard_password():
    try:
        user_length = int(input('Choose a length between 6 and 20: '))
    except ValueError:
        print('Enter a valid number!')
        return

    random_pw = ''
    en_alphabet = list(string.ascii_lowercase)
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    special_symbols = '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'
    for i in range(1, user_length + 1):
        char_mode = random.randrange(3)

        if char_mode == 0:  # we add a letter ( uppercase or lowercase)
            random_letter_index = random.randint(1, 25)
            case_switch = random.randint(0, 1)
            if case_switch == 1:  # we add an uppercase letter
                random_pw += en_alphabet[random_letter_index].upper()
            else:  # we add a lowercase letter
                random_pw += en_alphabet[random_letter_index]
        elif char_mode == 1:  # we add a random digit
            random_digit_index = random.randrange(10)
            random_pw += str(digits[random_digit_index])
        elif char_mode == 2:  # we add a random symbol
            random_symbol_index = random.randrange(32)
            random_pw += special_symbols[random_symbol_index]
    return random_pw


def generate_random_easy_password():
    try:
        user_input = int(input(
            'Do you want it to be one word or two words? Enter 1 or 2 (a larger number than 2 will result in a 2-word '
            'password): '))
    except ValueError:
        print('Invalid number...')
        return
    random_pw = ''
    word_file = "/usr/share/dict/words"
    dict_words = open(word_file).read().splitlines()
    if user_input == 1:
        random_word_index = random.randint(0, len(dict_words))
        random_pw += dict_words[random_word_index]
    else:
        for n in range(2):
            random_word_index = random.randint(0, len(dict_words))
            random_pw += dict_words[random_word_index]
    return random_pw


if __name__ == '__main__':
    ask_user()
