def addBruh(myWords):
	modifiedWords = "Bruh " + myWords
	return modifiedWords

# test function
sentence = "I want a cat." 
newSentence = addBruh(sentence)

print("The old sentence: " + sentence)
print("The new sentence: " + newSentence)

# doesn't print
print(modifiedWords)
