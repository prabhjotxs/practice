import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#link = input('Enter URL: ')
s_count = input('Enter count: ')
count = int(s_count)
s_position = input('Enter position: ')
position = int(s_position)
#link = 'http://py4e-data.dr-chuck.net/known_by_Safiya.html'

while count>=0:
    pieces = link.split('_')
    name_html = pieces[2].split('.')
    name = name_html[0]
    html = urllib.request.urlopen(link).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    lp = position
    for tag in tags:
        link = tag.get('href', None)
        if (lp == 1):
            break
        lp = lp - 1
    count = count - 1

if count is -1:
    print(name)