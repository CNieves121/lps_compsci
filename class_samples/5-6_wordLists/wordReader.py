# read all the words in Dictionary.txt into a list
wordsFile = open("Dictionary.txt", "r")
wordsList = []

myWord = wordsFile.readline()
# as long as there are more words, put the word in the list and read another
while myWord != "":
	wordsList.append(myWord)
	myWord = wordsFile.readline()
print(wordsList[0])
