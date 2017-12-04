"""
Exercise 3 from http://www.practicepython.org/
Take a list, say for example this one:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:

Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in
it and print out this new list. Write this in one line of Python. Ask the user for a number and return a list that
contains only elements from the original list a that are smaller than that number given by the user. """


def fib_generator():
    a, b = 0, 1
    yield 0
    while True:
        a, b = b, a + b
        yield a


def nums_lt(nums):
    user_number = int(input('Enter a threshold: '))
    new_nums = [n for n in nums if n < user_number]
    return new_nums


if __name__ == '__main__':

    fibonacci_numbers = []
    fib = fib_generator()
    for n in range(12):
        fibonacci_numbers.append(next(fib))
    print(fibonacci_numbers)
    print(nums_lt(fibonacci_numbers))
