import urllib2
from BeautifulSoup import BeautifulSoup
import emotionMain

for i in range(1,13):
    print ('\nMonth '+ str(i))

    #Months with 31 days
    # if(i==1 or i==3 or i==4 or i==6 or i==8 or i==10 or i==11):
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