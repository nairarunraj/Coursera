# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# Python3

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

def navigate_to_url(url, count, position):
    print('Retrieving ' + url)

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    url = soup('a')[position - 1].get('href', None)

    if(count==0): return

    navigate_to_url(url, count - 1, position)

count = int(input('Enter count: '))
position = int(input('Enter position: '))
#count = 7
#position = 18

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
#url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
#url = 'http://py4e-data.dr-chuck.net/known_by_Jensyn.html'
navigate_to_url(url, count, position)
