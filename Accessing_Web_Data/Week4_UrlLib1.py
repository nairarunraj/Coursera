## Week3_UrlLib.py
## Read the txt file using urllib
## Extract the following tags-
##   'Last-Modified', 'ETag', 'Content-Length', 'Cache-Control', 'Content-Type'


import pprint
import re
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')

header = dict()

for line in fhand:
    line = line.decode().strip()
    for headerTag in ('Last-Modified', 'ETag', 'Content-Length', \
    'Cache-Control', 'Content-Type'):
        matchedStringList = re.findall(re.escape(headerTag) +
        r":\s+(.*)", line)
        if(len(matchedStringList) != 1): continue
        header[headerTag] = matchedStringList[0]

pprint.PrettyPrinter(indent=4).pprint(header)
