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
counts = dict(Counter(month_strings))

print(counts)

"""
Exercise 36 Birthday Plots

This exercise is Part 4 of 4 of the birthday data exercise series. The other exercises are: Part 1, Part 2, and Part 3.

In the previous exercise we counted how many birthdays there are in each month in our dictionary of birthdays.

In this exercise, use the bokeh Python library to plot a histogram of which months the scientists have birthdays in!
"""
from bokeh.plotting import figure, show, output_file
# we specify an HTML file where the output will go
output_file("scientist_birthmonths.html")

# load our x and y data
x_categories = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
                "October", "November", "December"]
x_axis = [k for k in counts.keys()]
y_axis = [v for v in counts.values()]


# create a figure
plot = figure(x_axis_label='Months', y_axis_label='Number of Scientists born', title='Months scientists have '
                                                                                     'birthdays in',
              plot_width=900, plot_height=600, x_range=x_categories)

# create a histogram
plot.vbar(x=x_axis, top=y_axis, width=0.5)

# render (show) the plot
show(plot)
