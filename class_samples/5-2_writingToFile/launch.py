#opens walking instructions text file
walking_file = open("walkingInstructions.txt", "r")
# sets variable that reads line by line
lineToPrint = walking_file.readline()
# makes it so as long as there is some text left, it will read the line, otherwise it stops running
while lineToPrint != "":
	# adds "duh" to the end of lines
	print(lineToPrint + ", duh")
	#prints line by line
	lineToPrint = walking_file.readline()
