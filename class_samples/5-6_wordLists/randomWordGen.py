
import random

myFile = open("Dictionary.txt", "r")

myList = []


myWord = myFile.readline()

while myWord != "":
	myList.append(myWord)
	myWord = myFile.readline()
listNum = len(myList) - 1
myRand = random.randint(0, listNum)
print(myList[myRand])
