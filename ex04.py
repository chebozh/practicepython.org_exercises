"""Exercise 4 from http://www.practicepython.org/
Create a program that asks the user for a number and then prints
out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides
evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""


def get_divisors(number):
    divisors = [n for n in range(1, number + 1) if number % n == 0]
    return divisors


if __name__ == '__main__':
    try:
        user_number = int(input('Enter a number to get the divisors for: '))
    except ValueError:
        print('Enter a valid number pls.')
    print(get_divisors(user_number))
