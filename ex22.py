"""
Exercise 22 from http://www.practicepython.org
Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file,
and print out the results to the screen. I have a .txt file for you, if you want to use it!

Extra:

Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file,
and count how many of each “category” of each image there are.
"""
names_dict = {}
with open('ex22_file.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        line = line.strip()
        if line in names_dict:
            names_dict[line] += 1
        else:
            names_dict[line] = 1
        line = open_file.readline()

print(names_dict)

# extra task:
categories_dict = {}
with open('ex22_file_extra.txt', "r") as file:
    line = file.readline()
    while line:
        line = line[3:-26]
        if line in categories_dict:
            categories_dict[line] += 1
        else:
            categories_dict[line] = 1
        line = file.readline()

print(categories_dict)
