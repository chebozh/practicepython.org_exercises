"""
Exercise 14 from http://www.practicepython.org/

Write a function that takes a list and returns a new list that contains
all the elements of the first list minus duplicates.
"""


def remove_duplicates(dup_list):
    new_list = []
    for n in dup_list:
        if n not in new_list:
            new_list.append(n)
    return new_list

# OR:


def remove_duplicates_easier(dup_list):
    return list(set(dup_list))


if __name__ == '__main__':
    duplicated = [1, 2, 3, 4, 5, 1, 5]
    non_duplicated = remove_duplicates(duplicated)
    non_duplicated2 = remove_duplicates_easier(duplicated)
    print(duplicated)
    print(non_duplicated)
    print(non_duplicated2)
