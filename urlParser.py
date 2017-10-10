import urllib2
from BeautifulSoup import BeautifulSoup
import urlContentParser

baseUrl = 'https://echelog.com/logs/browse/angularjs/'
extraUrl = []
url = []

#Putting the extraUrls into the extraUrl list.
opener = urllib2.build_opener()
ourUrl = opener.open(baseUrl+'1475272800').read()
soup = BeautifulSoup(ourUrl)
numberList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for eachA in soup.findAll('a'):
    firstChar = (str(eachA.get('href')))[0]
    if(firstChar in numberList):
        extraUrl.append(eachA.get('href'))

#Editing the extraUrl list.
for i in range(0,3):
    extraUrl.pop(0)
extraUrl.pop()
del extraUrl[32:]
extraUrl.pop()

#Populating url list.
for i in range(0,len(extraUrl)):
    url.append(baseUrl + extraUrl[i])

#Calling urlContentParser
urlContentParser.urlContentParser(url)