# Exercise 2 from http://www.practicepython.org/
# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the
# user.
#
# Hint: how does an even / odd number react differently when divided by 2?
#
# Extras:
#
# If the number is a multiple of 4, print out a different message. Ask the user for two numbers: one number to check
# (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not,
#  print a different appropriate message.


def odd_even():
    try:
        user_number = int(input('Enter a number: '))
    except ValueError:
        print('Enter an integer not a string.')

    if user_number % 4 == 0:
        print('The entered number is a multiple of 4. Bye.')
    elif user_number % 2 == 0:
        print('The entered number is even. Bye.')
    else:
        print('The entered number is odd. Bye. ')


def two_numbers():
    try:
        num = int(input('Enter a number to check: '))
        check = int(input('Enter a number to divide by: '))
    except ValueError:
        print('Enter a valid number.')

    if num % check == 0:
        print(str(check) + ' divides evenly into ' + str(num))
    else:
        print(str(check) + ' doesn\'t divide evenly into ' + str(num))


if __name__ == '__main__':
    odd_even()
    two_numbers()
