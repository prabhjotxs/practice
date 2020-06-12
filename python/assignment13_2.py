import urllib.request, urllib.parse, urllib.error
import json

count = 0

link = input('Enter location: ')
print('Retrieving ' + link)

uh = urllib.request.urlopen(link)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

js = json.loads(data)
print('Count:', len(js['comments']))

for item in js['comments']:
    count = count + item['count']

print('Sum:', count)