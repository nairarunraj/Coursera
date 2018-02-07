## Week6- Extracting data from JSON
## python3 Week6_ExtractingFromJson.py

import pprint
import urllib.request, urllib.parse, urllib.error
import json

while True:
    url = input('Enter location: ')
    #url = 'http://py4e-data.dr-chuck.net/comments_17693.json'
    if len(url) < 1: break

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    #print(data.decode())

    comments = json.loads(data.decode())

    print('Count:', str(len(comments['comments'])))

    sum = 0
    for names in comments['comments']:
        sum = sum + int(names['count'])

    print('Sum:', str(sum))
