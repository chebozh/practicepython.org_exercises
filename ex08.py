"""
Exercise 8 from http://www.practicepython.org/

Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""
import getpass

stats = {'player1': 0,
         'player2': 0}


def ask_for_input():
    while True:
        player1 = getpass.getpass('Player 1, please enter rock/paper/scissors: ')
        player2 = getpass.getpass('Player 2, please enter rock/paper/scissors: ')
        compare(player1, player2)
        user_command = input('Type "quit" to end the game or press enter to play again: ')
        if user_command == 'quit':
            print('Bye!')
            break


def compare(p1, p2):
    if p1 == p2:
        print('Draw!')
    elif (p1 == 'rock' and p2 == 'scissors') or (p1 == 'paper' and p2 == 'rock') or (
                    p1 == 'scissors' and p2 == 'paper'):
        print('Player 1 wins!')
        print(update_scores('player1'))
    elif (p2 == 'rock' and p1 == 'scissors') or (p2 == 'paper' and p1 == 'rock') or (
                    p2 == 'scissors' and p1 == 'paper'):
        print('Player 2 wins!')
        print(update_scores('player2'))
    else:
        print('Something went wrong!')


def update_scores(winner):
    stats[winner] += 1

    return stats


if __name__ == '__main__':
    ask_for_input()
