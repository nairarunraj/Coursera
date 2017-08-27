## Week3_Socket1.py
## Read the txt file using socket
## Extract the following tags-
##   'Last-Modified', 'ETag', 'Content-Length', 'Cache-Control', 'Content-Type'


import pprint
import re
import socket

# socket.AF_INET is used for an IPv4 host
# socket.SOCK_STREAM is generally used as the port
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

header = dict()

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    lines = data.decode().split('\n')

    for line in lines:
        line = line.strip()
        for headerTag in ('Last-Modified', 'ETag', 'Content-Length', \
                            'Cache-Control', 'Content-Type'):
            matchedStringList = re.findall(re.escape(headerTag) +
                    r":\s+(.*)", line)
            if(len(matchedStringList) != 1): continue
            header[headerTag] = matchedStringList[0]

mysock.close()

pprint.PrettyPrinter(indent=4).pprint(header)
