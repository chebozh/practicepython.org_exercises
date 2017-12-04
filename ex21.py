"""
Exercise 21 from http://www.practicepython.org

Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with some different
code, use the code from the solution), and instead of printing the results to a screen, write the results to a txt
file. In your code, just make up a name for the file you are saving to.

Extras:

Ask the user to specify the name of the output file that will be saved.
"""
import requests
from bs4 import BeautifulSoup


base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")
filename = input('Enter a name for the file: ')

with open(filename, 'w') as file:
    for story_heading in soup.find_all(class_="story-heading"):
        if story_heading.a:
            file.write(story_heading.a.text.replace("\n", " ").strip())
        else:
            file.write(story_heading.contents[0].strip())

# OR:
#
#
# heading_list = []
#
# url = 'https://www.nytimes.com/'
# r = requests.get(url)
# soup = BeautifulSoup(r.content, "html.parser")
# headings = soup.find_all('h2', 'story-heading')
#
# filename = input('Enter a name for the file ending with .txt: ')
#
# with open(filename, 'w') as file:
#     for heading in headings:
#         if heading:
#             file.write(heading.text.replace("\n", " ").strip())
#



