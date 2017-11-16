import urllib2
from BeautifulSoup import BeautifulSoup
import emotionMain
import csv

for i in range(1,2):
    print ('\nMonth '+ str(i))

    for j in range(32):
        try:
            with open("sites/" + str(i) + "_" + str(j+1) + ".html", "r") as reader:
                print ('Processing File ' + str(j+1))
                soup = BeautifulSoup(reader.read())
                spanList = soup.findAll('span')
                outFile = open('C://Users//lenovo//PycharmProjects//GAEmotion//Result//' + str(i) + "//" + str(j + 1) + '.txt', 'w')

                for eachSpan in spanList:
                    if (eachSpan['class'] == "d"):
                        outFile.write(str(eachSpan.string).replace('&lt;', "").replace('&gt;', ":") + "\n")

                fileName = 'C://Users//lenovo//PycharmProjects//GAEmotion//Result//' + str(i) + "//" + str(j + 1) + '.txt'
                emotionMain.fileEmotions(fileName)

                print('Processing of File ' + str(j+1) + " Completed.")
        except Exception:
            pass

    if i==3:
        emotionMain.printDominatingEmotion()