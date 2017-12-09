"""
This exercise is Part 3 of 4 of the birthday data exercise series. The other exercises are: Part 1, Part 2, and Part 4.

In the previous exercise we saved information about famous scientists’ names and birthdays to disk. In this exercise, load that JSON file from disk, extract the months of all the birthdays, and count how many scientists have a birthday in each month.

Your program should output something like:

        {
            "May": 3,
            "November": 2,
            "December": 1
        }

"""
import json
import re
from collections import Counter

birthdays = {}
with open("ex34_birthdays.json", "r") as f:
    birthdays = json.load(f)

month_lists = [re.findall(r"(?i)\b[a-z]+\b", n) for n in birthdays.values()]
month_strings = [n[0] for n in month_lists]

print(Counter(month_strings))
