## Week5 - Extracting Data from XML
## pip3 install defusedxml
## python3 Week5_ExtractingFromXML.py

import pprint
import urllib.request, urllib.parse, urllib.error
import defusedxml.ElementTree as ET

while True:
    url = input('Enter location: ')
    #url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
    if len(url) < 1: break

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    #print(data.decode())
    tree = ET.fromstring(data)

    #print(ET.tostring(tree))
    results = tree.findall('.//count')

    print('Count:', str(len(results)))
    sum = 0
    for count in results:
        sum = sum + int(count.text)

    print('Sum:', str(sum))
