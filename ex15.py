"""
Ex 15 rom http://www.practicepython.org/ Write a program (using functions!) that asks the user for a long string
containing multiple words. Print back to the user the same string, except with the words in backwards order. For
example, say I type the string:

  My name is Michele

Then I would see the string:

  Michele is name My

shown back to me.
"""


def ask_user_for_string():
    user_string = input('Enter a long string (sentence) to be reversed: ')
    return user_string


def reverse_string(string):
    string_list = string.split()
    return " ".join(reversed(string_list))


if __name__ == '__main__':
    user_input = ask_user_for_string()
    print(reverse_string(user_input))
