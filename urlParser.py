import urllib2
from BeautifulSoup import BeautifulSoup
# import urlContentParser

# 2016-17
# 1. October - 1475272800
# 2. November - 1477954800
# 3. December - 1480546800
# 4. January - 1483225200
# 5. February - 1485903600
# 6. March - 1488322800
# 7. April - 1490997600
# 8. May - 1493589600
# 9. June - 1496268000
# 10. July - 1498860000
# 11. August - 1501538400
# 12. September - 1504216800

baseUrl = 'https://echelog.com/logs/browse/angularjs/'
initialUrl = ['1475272800','1477954800','1480546800','1483225200','1485903600','1488322800','1490997600','1493589600','1496268000','1498860000','1501538400','1504216800']
url = []
numbers = []
for i in range(32):
    numbers.append(str(i))

for eachMonth in range(0,12):

    opener = urllib2.build_opener()
    ourUrl = opener.open(baseUrl + initialUrl[eachMonth]).read()
    soup = BeautifulSoup(ourUrl)

    links = {}
    for a in soup.findAll("a"):
        if (a.text in numbers):
            links[a.text] = a.get("href")

    #Populating url list.
    for i in links.keys():
        url.append(baseUrl + links[i])

    for i in enumerate(url):
        with open("sites/" + str(eachMonth + 1) + "_" + str(i[0] + 1) + ".html", "w") as writer:
            opener = urllib2.build_opener()
            ourUrl = opener.open(i[1]).read()
            soup = BeautifulSoup(ourUrl)
            writer.write(str(soup))

    url = []
