"""
Exercise 11 from http://www.practicepython.org/
Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten,
a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you.
 """


def get_integer():
    return int(input("Enter a number to check for primality: "))


def is_prime(num):
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                print(i, "times", num // i, "is", num)
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")


if __name__ == '__main__':
    try:
        user_number = get_integer()
    except ValueError:
        print('Enter a valid number.')

    is_prime(user_number)
