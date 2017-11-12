from bs4 import BeautifulSoup
import csv

#Declaring variables
emo = {'Anger':0, 'Anticipation':0, 'Disgust':0, 'Fear':0, 'Joy':0, 'Sadness':0, 'Surprise':0, 'Trust':0}
textList = []
finalResult = []

print "Processing...\n"

#Opening and reading file
def fileEmotions(outFile):
    file = open(outFile)
    file = file.read()

    #Removing special characters from the text
    file = file.replace(".", "")
    file = file.replace(",", "")
    file = file.replace("!", "")
    file = file.replace("?", "")

    #Storing words from the text into a list
    def split_sentence(input):
        words = input.split()
        for i in words:
            textList.append(i)

    split_sentence(file)

    #Increasing the counter of the emotion.
    def incrementCounter(j):
        if j == 0:
            emo['Anger'] = emo['Anger'] + 1
        if j == 1:
            emo['Anticipation'] = emo['Anticipation'] + 1
        if j == 2:
            emo['Disgust'] = emo['Disgust'] + 1
        if j == 3:
            emo['Fear'] = emo['Fear'] + 1
        if j == 4:
            emo['Joy'] = emo['Joy'] + 1
        if j == 5:
            emo['Sadness'] = emo['Sadness'] + 1
        if j == 6:
            emo['Surprise'] = emo['Surprise'] + 1
        if j == 7:
            emo['Trust'] = emo['Trust'] + 1

    with open('emotionDatabase.csv', "r") as f:
        mycsv = csv.reader(f)
        for i, row in enumerate(mycsv):
            for j, col in enumerate(row):
                for eachword in textList:
                    if eachword == col:
                        incrementCounter(j)

def printDominatingEmotion():
    #Printing the count of each emotion in the text
    print ("Angry: " + str(emo['Anger']))
    print ("Anticipation: " + str(emo['Anticipation']))
    print ("Disgust: " + str(emo['Disgust']))
    print ("Fear: " + str(emo['Fear']))
    print ("Joy: " + str(emo['Joy']))
    print ("Sadness: " + str(emo['Sadness']))
    print ("Surprise: " + str(emo['Surprise']))
    print ("Trust: " + str(emo['Trust']))

    #Conclusion
    maximum = max(emo['Anger'], emo['Anticipation'], emo['Disgust'], emo['Fear'], emo['Joy'], emo['Sadness'], emo['Surprise'], emo['Trust'])
    for key, value in emo.iteritems():
        if(value == maximum):
            finalResult.append(key)

    if(finalResult.__len__() == 1):
        print ("\n The dominating emotion is " + str(*finalResult) + ".")

    elif(finalResult.__len__() > 1):
        print ("\n The dominating emotions are " + ', '.join(finalResult) + ".")