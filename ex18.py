# Ex 18
# Create a program that will play the “cows and bulls” game with the user. The game works like this:
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed
# correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is
#  a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user
# guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh
# game and tell the user at the end.


import random

guesses = 0


def ask_user():
    while True:
        user_input = input('Enter a 4-digit number or "q" to quit : ')
        if user_input == 'q':
            print('Bye')
            break
        else:
            print(cows_and_bulls(user_input))


def cows_and_bulls(user_num):
    global guesses
    cows = 0
    bulls = 0
    user_num = str(user_num)
    magic_number = str(random.randint(1000, 9999))
    for n in user_num:
        if n in magic_number:
            if user_num.index(n) == magic_number.index(n):
                cows += 1
            else:
                bulls += 1
    guesses += 1
    return 'The number was: ' + str(magic_number) + '. You get ' + str(cows) + ' cows, ' + str(bulls) + ' bulls' \
           + '. This was guess number :' + str(guesses)


if __name__ == '__main__':
    ask_user()
