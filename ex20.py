# Exercise 20 from http://www.practicepython.org
# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to
# largest) and another number. The function decides whether or not the given number is inside the list and returns (
# then prints) an appropriate boolean.
#
# Extras:
# Use binary search.
import random


def binary_search(ordered_list, element):
    # base case
    if len(ordered_list) == 0:
        return False
    else:
        middle = len(ordered_list) // 2
        if element == ordered_list[middle]:
            return True
        else:
            if element < ordered_list[middle]:
                return binary_search(ordered_list[:middle], element)
            else:
                return binary_search(ordered_list[middle + 1:], element)


if __name__=="__main__":
    list_length_1 = random.randint(1, 20)
    l1 = random.sample(range(0, 100), list_length_1)
    l1.sort()
    print(l1)
    print(binary_search(l1, 44))
