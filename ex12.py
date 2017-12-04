"""
Exercise 12 from http://www.practicepython.org/
Write a program that takes a list of numbers (for example, a = [5,  10, 15, 20, 25]) and makes
a new list of only the first and last elements of the given list.
For practice, write this code inside a function.
"""
import random


def list_ends(l):
    if len(l) <= 1:
        return l
    return [l[0], l[-1]]


if __name__ == '__main__':
    list_length = random.randint(1, 20)
    list1 = random.sample(range(1, 100), list_length)
    print(list1)
    print(list_ends(list1))

