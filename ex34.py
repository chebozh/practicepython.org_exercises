"""
Exercise 34 Birthday Json
This exercise is Part 2 of 4 of the birthday data exercise series. The other exercises are: Part 1, Part 3, and Part 4.

In the previous exercise we created a dictionary of famous scientists’ birthdays. In this exercise, modify your
program from Part 1 to load the birthday dictionary from a JSON file on disk, rather than having the dictionary
defined in the program.

Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary, and update the JSON file you
have on disk with the scientist’s name. If you run the program multiple times and keep adding new names,
your JSON file should keep getting bigger and bigger.
"""
import json

birthdays = {}
with open("ex34_birthdays.json", "r") as f:
    birthdays = json.load(f)


def ask_user():
    while True:
        user_input = input('Would you like to get or add a birthday? Enter "get", "add" or q to quit: ')
        if user_input == 'q':
            print('Bye!')
            break
        elif user_input == 'add':
            add_entry()
        elif user_input == 'get':
            get_json()
        else:
            print('Invalid command.')


def add_entry():
    name = input('Enter scientist’s name: ')
    birth_date = input('Enter scientist’s birthday in format Month date, year (like March 14, 1879): ')
    birthdays[name] = birth_date
    with open("ex34_birthdays.json", "w") as f:
        json.dump(birthdays, f)

    another = input('Want to add another? Enter "y" to add or "n" to exit')
    if another == 'y':
        add_entry()
        print('Added entry/ies!.')
    else:
        print('Added entry/ies!.')
        return


def get_json():
    print('Welcome to the birthday dictionary. We know the birthdays of: ')
    for n in birthdays.keys():
        print(n)
    user_input = input('Who\'s birthday do you want to look up? ').strip()
    if user_input in birthdays:
        print('{}\'s birthday is {}'.format(user_input, birthdays[user_input]))
    else:
        print('Person birthday not available.')

if __name__ == '__main__':
    ask_user()

