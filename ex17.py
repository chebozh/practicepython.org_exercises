# # Exercise 12 from http://www.practicepython.org/
# Use the BeautifulSoup and requests Python packages to print out a
# list of all the article titles on the New York Times homepage.

import requests
from bs4 import BeautifulSoup

heading_list = []

url = 'https://www.nytimes.com/'
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
headings = soup.find_all('h2', 'story-heading')


for heading in headings:
    heading_list.append(heading.text.replace("\n", " ").strip())

print(heading_list)


