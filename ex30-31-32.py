"""
Exercise 30

This exercise is Part 1 of 3 of the Hangman exercise series. The other exercises are: Part 2 and Part 3.
In this exercise, the task is to write a function that picks a random word from a list of words from the SOWPODS
dictionary. Download this file and save it in the same directory as your Python code.
This file is Peter Norvig’s compilation of the dictionary of words used in professional Scrabble tournaments.
Each line in the file contains a single word.
"""
import random


def make_wordlist(filename):
    words = []
    with open(filename, 'r') as f:
        line = f.readline().strip()
        while line:
            words.append(line)
            line = f.readline().strip()
    return words


def pick_random_word(wordlist):
    return random.choice(wordlist)


"""
Exercises 31 and 32 In this exercise, we will finish building Hangman. In the game of Hangman, the player only has 
6 incorrect guesses (head, body, 2 legs, and 2 arms) before they lose the game.
 Only let the user guess 6 times, and tell the user how many guesses they have left. 
 Keep track of the letters the user guessed. If the user guesses a letter they already guessed, 
 don’t penalize them - let them guess again. 
"""


def game_loop(random_word):
    print('Welcome to Hangman!')
    correct_word = random_word
    letters = list('_' * len(random_word))
    guesses = 0
    lives = 6
    letters_tried = []

    while True:
        print(' '.join(letters))
        print()
        guess = input('Guess your letter or enter @ to exit: ').upper()
        guesses += 1

        if guess not in letters_tried:
            letters_tried.append(guess)
        else:
            print('You\'ve already tried that letter. Try again.')
            continue

        if guess == '@':
            print('Bye!')
            break
        elif guess in correct_word:
            indexes = [pos for pos, char in enumerate(correct_word) if char == guess]
            for i in indexes:
                letters[i] = guess
        else:
            lives -= 1
            if lives > 0:
                print('Incorrect! Tries left: {}'.format(lives))
            else:
                print('You lost! No more tries left. The word was {}'.format(correct_word))
                again = input('Do you want to play again? Enter "y" to play again or "n" to quit: ')
                if again.strip() == 'y':
                    set_game(words)
                else:
                    print('Bye!')
                    break

        if '_' not in letters:
            print('You won! The word was {}. That took you {} times'.format(''.join(letters), guesses))
            again = input('Do you want to play again? Enter "y" to play again or "n" to quit: ')
            if again == 'y':
                set_game(words)
            else:
                print('Bye!')
                break


def set_game(words_list):
    random_word = pick_random_word(words_list)
    game_loop(random_word)


if __name__ == '__main__':
    words = make_wordlist('sowpods.txt')
    set_game(words)
