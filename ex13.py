"""
Exercise 13 from http://www.practicepython.org/

# Write a program that asks the user how many Fibonacci numbers to generate and then generates them.
"""


def fib_generator():
    a, b = 0, 1
    yield 0
    while True:
        a, b = b, a + b
        yield a


def ask_user_and_generate_fib():
    how_many = int(input('How many Fibonacci numbers do you want to be generated?: '))
    fibonacci_numbers = []
    fib = fib_generator()
    for n in range(how_many):
        fibonacci_numbers.append(next(fib))
    print(fibonacci_numbers)


if __name__ == '__main__':
    ask_user_and_generate_fib()
