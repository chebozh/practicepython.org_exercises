"""
Exercise 33 Birthday Dictionaries

This exercise is Part 1 of 4 of the birthday data exercise series. The other exercises are: Part 2, Part 3, and Part 4.

For this exercise, we will keep track of when our friend’s birthdays are, and be able to find that information based
on their name. Create a dictionary (in your file) of names and birthdays. When you run your program it should ask the
user to enter a name, and return the birthday of that person back to them.
"""


def get_birthday():
    birthdays = {
        'Albert Einstein': 'March 14, 1879',
        'Benjamin Franklin': 'January 17, 1706',
        'Ada Lovelace': 'December 10, 1815'
    }
    print('Welcome to the birthday dictionary. We know the birthdays of: ')
    for n in birthdays.keys():
        print(n)
    user_input = input('Who\'s birthday do you want to look up? ').strip()
    if user_input in birthdays:
        print('{}\'s birthday is {}'.format(user_input, birthdays[user_input]))
    else:
        print('Person birthday not available.')

get_birthday()


