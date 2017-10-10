import urllib2
from BeautifulSoup import BeautifulSoup

opener = urllib2.build_opener()

def urlContentParser(urlList):
    for eachUrl in enumerate(urlList):
        ourUrl = opener.open(eachUrl[1]).read()
        soup = BeautifulSoup(ourUrl)
        spanList = soup.findAll('span')
        outFile = open('C://Users//lenovo//PycharmProjects//GAEmotion//Result//' + str(eachUrl[0]+1) + '.txt','w')

        for eachSpan in spanList:
            if (eachSpan['class'] == "d"):
                outFile.write(str(eachSpan.string).replace('&lt;',"").replace('&gt;',":") + "\n")