import urllib2
from BeautifulSoup import BeautifulSoup
import emotionMain

opener = urllib2.build_opener()

def urlContentParser(urlList, eachMonth):
    print ("\nMonth: " + str(eachMonth+1)+ "\n")
    for eachUrl in enumerate(urlList):
        print ("Processing file "+ str(eachUrl[0]+1) + "...")
        ourUrl = opener.open(eachUrl[1]).read()
        soup = BeautifulSoup(ourUrl)
        spanList = soup.findAll('span')
        outFile = open('C://Users//lenovo//PycharmProjects//GAEmotion//Result//' + str(eachMonth+1) + "//" + str(eachUrl[0]+1) + '.txt','w')

        for eachSpan in spanList:
            if (eachSpan['class'] == "d"):
                outFile.write(str(eachSpan.string).replace('&lt;',"").replace('&gt;',":") + "\n")

        fileName = 'C://Users//lenovo//PycharmProjects//GAEmotion//Result//' + str(eachMonth+1) + "//" + str(eachUrl[0]+1) + '.txt'
        emotionMain.fileEmotions(fileName)

    if(eachMonth == 11):
        emotionMain.printDominatingEmotion()