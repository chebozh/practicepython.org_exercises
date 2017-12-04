"""Exercise 6 from http://www.practicepython.org/
 Ask the user for a string and print out whether this string is a
palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
"""


def is_palindrome(string):
    string_list = list(string)
    string_list_reversed = list(reversed(string_list))

    if string_list == string_list_reversed:
        print("This word is a palindrome")
        print('It is spelled ' + "".join(string_list_reversed) + ' both backwards and forwards')
    else:
        print("This word is not a palindrome")
        print('Backwards it is spelled ' + "".join(string_list_reversed))


user_word = str(input('Enter a word to check: '))
is_palindrome(user_word)
