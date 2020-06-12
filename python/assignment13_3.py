import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

address = input('Enter location: ')
if len(address) < 1:
    print('Address error')
    quit()

parms = dict()
parms['address'] = address
if api_key is not False:
    parms['key'] = api_key

url = serviceurl + urllib.parse.urlencode(parms)
print('Retrieving', url)

uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(data)

place_id = js['results'][0]['place_id']
print('place_id', place_id)
