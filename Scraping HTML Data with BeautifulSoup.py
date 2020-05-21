import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
url = 'http://py4e-data.dr-chuck.net/comments_385757.html'
html = urllib.request.urlopen(url).read()
#print("html is ", html)
soup = BeautifulSoup(html, 'html.parser')
span = soup('span')
print("spans are", span)
#<span class="comments">26</span>
res = 0
for aspan in span:
    res = res + int(aspan.get_text())
    print("res is",res)
print(res)

'''
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
url = 'http://py4e-data.dr-chuck.net/comments_42.html '
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tag = soup("span")
count=0
sum=0
for i in tag:
	x=int(i.text)
	count+=1
	sum = sum + x
print(count)
print (sum)

'''