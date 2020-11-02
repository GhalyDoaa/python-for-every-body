#Scraping HTML Data with BeautifulSoup
#Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program similar to http://#www.py4e.com/code3/urllink2.py. The program will use urllib to read the HTML from the data files below, and parse #the data, extracting numbers and compute the sum of the numbers in the file.﻿
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
url = 'http://py4e-data.dr-chuck.net/comments_385757.html'
html = urllib.request.urlopen(url).read()
#print("html is ", html)
soup = BeautifulSoup(html, 'html.parser')
spans = soup('span')
#<span class="comments">26</span>
print("spans are", spans)
response = 0
for span in spans:
    response = response + int(span.get_text())
    print("response is",response)
print(response)


