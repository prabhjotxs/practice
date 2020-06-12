import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
total = 0

html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_233493.html').read()

soup = BeautifulSoup(html, 'html.parser')
tags = soup('span')

for tag in tags:
    number = tag.text
    total = total + int(number)

print(total)
