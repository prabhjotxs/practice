import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

#link = input('Enter location: ')
link = 'http://py4e-data.dr-chuck.net/comments_233495.xml'
print('Retrieving ' + link)

xml_data = urllib.request.urlopen(link).read()
print('Retrieved', len(xml_data), 'characters')

tree = ET.fromstring(xml_data)
comments = tree.findall('comments/comment')
print('Count:', len(comments))

total = 0
for comment in comments:
    count = comment.find('count').text
    total = total + int(count)
    
print('Sum:', total)