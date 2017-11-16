import urllib2
from BeautifulSoup import BeautifulSoup
import emotionMain
import csv

month = ''
# Adding title row to 'EmotionGraph.csv'
with open('EmotionGraph.csv', 'w') as f:
    theWriter = csv.writer(f);
    theWriter.writerow(['','Anger', 'Anticipation', 'Disgust', 'Fear', 'Joy', 'Sadness', 'Surprise', 'Trust'])

for i in range(1,4):
    emotionMain.setEmoDictValuesToZero()

    if (i == 1):
        month = 'October'
    if (i == 2):
        month = 'November'
    if (i == 3):
        month = 'December'

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

    # Adding content to 'EmotionGraph.csv'
    with open('EmotionGraph.csv', 'a') as f:
        theWriter = csv.writer(f);
        theWriter.writerow([month, emotionMain.emo['Anger'], emotionMain.emo['Anticipation'], emotionMain.emo['Disgust'], emotionMain.emo['Fear'], emotionMain.emo['Joy'], emotionMain.emo['Sadness'], emotionMain.emo['Surprise'], emotionMain.emo['Trust']])

    if i==3:
        emotionMain.printDominatingEmotion()