"""
Exercise 5 from http://www.practicepython.org/
Take two lists, say for example these two:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] and write a program
that returns a list that contains only the elements that are common between the lists (without duplicates). Make
sure your program works on two lists of different sizes.
"""

import random


def list_overlap(list1, list2):
    common_elements = list(set(list1) & set(list2))
    return common_elements


list_length_1 = random.randint(1, 20)
list_length_2 = random.randint(1, 19)
a = random.sample(range(1, 100), list_length_1)
b = random.sample(range(1, 100), list_length_2)
print(a)
print(b)
print(list_overlap(a, b))
