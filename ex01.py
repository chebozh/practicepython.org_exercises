# Exercise 1 from http://www.practicepython.org/
# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that
# tells them the year that they will turn 100 years old.


import datetime


def greeting():
    today = datetime.datetime.today()
    name = str(input('Please enter your name... '))
    try:
        age = int(input('Please enter your age... '))
        magic_number = int(input('Please enter a magic number... '))
        year = today.year + (100 - age)
        message = 'Hi ' + name + '. You\'ll be a 100 years old in ' + str(year) + '\n'
    except:
        print('Please enter a number not a string and try again.')
    print(message * magic_number)


if __name__ == '__main__':
    greeting()
