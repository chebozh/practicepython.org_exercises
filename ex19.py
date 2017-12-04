"""
Exercise 19 from http://www.practicepython.org/exercise/2014/07/14/19-decode-a-web-page-two.html

Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the
article on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

"""
import requests
from bs4 import BeautifulSoup


url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
paragraphs = soup.find_all('p')

for item in soup.find_all('div', {"class:", "dek"}):
    print(item.text)

for item in soup.find_all('section', {'class:', 'content-section'}):
    print(item.text)
