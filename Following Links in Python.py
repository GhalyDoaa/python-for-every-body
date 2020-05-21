import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
count = int(input('Enter Count:'))
position = int(input('Enter Position:')) - 1
flag = int(input('''Select Url:
1: http://py4e-data.dr-chuck.net/known_by_Fikret.html
2: http://py4e-data.dr-chuck.net/known_by_Cohen.html
'''))
if flag == 1:
    url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
else:
    url = 'http://py4e-data.dr-chuck.net/known_by_Tom.html'
while True:
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    atags = soup('a')
    #print("atags are" ,atags) #list of a tags
    #<a href="http://py4e-data.dr-chuck.net/known_by_Aimee.html">Aimee</a>
    href = atags[position].get('href', None)
    #print("href is ",href)
    #http://py4e-data.dr-chuck.net/known_by_Paulina.html
    if href is None:
        print('runtime error')
        quit()
    if count > 1:
        # reduce the count
        # swap the url value with the new one and
        # start over applying all changes on the new url
        count = count - 1
        url = href
    else:
        #the main action
        res = atags[position].get_text()
        break
print(res)

'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url ='http://py4e-data.dr-chuck.net/comments_42.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
'''