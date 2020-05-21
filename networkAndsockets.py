# Search for lines that start with From and have an at sign
import urllib.request, urllib.parse, urllib.error
import re
#import BeautifulSoup
print(ord('G'))
print(chr(108))

print(chr(105))

url = 'http://data.pr4e.org/page1.htm'
html = urllib.request.urlopen(url).read()

links = re.findall(b'href="(http://.*?)"', html)
for link in links:
    print(link.decode())
#html = urllib.request.urlopen(url).read()
#soup = BeautifulSoup(html, 'html.parser')
#x = soup('a')













"""
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("data.pr4e.org", 80))
#transform to utf-8
cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n".encode()
mysock.send(cmd)
while True:
    data = mysock.recv(512)
    #if fetched data is nothing then we reached the end of it
    if (len(data) < 1):
        break
    #to get unicode
    print(data.decode())
mysock.close()




"""



"""


import urllib.request,urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())



import socket
import time

HOST="data.pr4e.org"
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
mysock.sendall(b"GET http://data.pr4e.org/cover.jpg HTTP/1.0\n\n")
count = 0
picture = b""
while True:
    data = mysock.recv(5120)
    if (len(data) < 1): break
    time.sleep(0.25)
    count = count + len(data)
    print(len(data), count)
    picture = picture + data
    print("pic is ", picture)

mysock.close()
# Look for the end of the header (2 CRLF)
pos = picture.find(b"\r\n\r\n")
print("Header length", pos)
print(picture[:pos].decode())
# Skip past the header and save the picture data
picture = picture[pos+4:]
fhand = open("stuf.jpg", "wb")
fhand.write(picture)
fhand.close()
# Code: http://www.py4e.com/code3/urljpeg.py
"""
