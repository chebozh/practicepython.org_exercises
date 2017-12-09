"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them
whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very
first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""
import random


def game_loop():
    magic_number = random.randint(1, 9)
    guess = 0
    attempts = 0

    while guess != magic_number and guess != "exit":
        guess = input("Enter a guess between 1 to 9: ")

        if guess == "exit":
            break

        guess = int(guess)
        attempts += 1

        if guess < magic_number:
            print("Too low")
        elif guess > magic_number:
            print("Too high")
        else:
            print("Right!")
            print("You took only", attempts, "tries!")


game_loop()
