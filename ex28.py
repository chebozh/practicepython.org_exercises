"""
Exercise 28

Implement a function that takes as input three variables, and returns the largest of the three. Do this without using
the Python max() function!

The goal of this exercise is to think about some internals that Python normally takes care of for us. All you need is
some variables and if statements!

"""


def get_max(a, b, c):
    if a == b and b == c:
        return 'all equal'
    elif a >= b and a >= c:
        return 'a: ' + str(a)
    elif b >= a and b >= c:
        return 'b: ' + str(c)
    else:
        return 'c: ' + str(c)


print(get_max(24, 12, 42))
