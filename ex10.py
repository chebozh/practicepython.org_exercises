"""
Exercise 10 from http://www.practicepython.org/
Take two lists, say for example these two:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] and write a program  that
returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your
program works on two lists of different sizes. Write this in one line of Python using at least one list
comprehension.
"""
import random


list_length_1 = random.randint(1, 20)
list_length_2 = random.randint(1, 19)

list1 = random.sample(range(1, 100), list_length_1)
list2 = random.sample(range(1, 100), list_length_2)

print(list1)
print(list2)

result1 = [i for i in set(list1) if i in list2]
# OR:
result2 = list(set(list1).intersection(list2))

print(result1)
print(result2)
