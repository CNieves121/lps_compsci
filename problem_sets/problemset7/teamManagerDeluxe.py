myPlayers = []
class Player(object):
	def __init__(self, name, age, goals, position):
		self.name = name
		self.age = age
		self.goals = goals
		self.position = position
	def getStats(self, name, age, goals):
		summary = "Name: " + self.name + "\n" + "Age: " + self.age + "\n" + "Goals: " + self.goals + "/n" + "Position: " + self.position
		return summary
	def saveTeam(self, filename):
# open the file
		myFile = open(filename, "w")
# write to the file
		for a in myPlayers:
			myFile.write(a.name + " " + a.age + " " + a.goals + " " + a.position)
# close the file
		myFile.close()
		
	def loadTeam(filename):
# create empty list
		myPlayers = []
# open the file
		myFile = open(filename, "r")
		
		splitThing = myFile.split(" ")
		while mySplit != "":
			mySplit = splitThing.split("")
			myPlayers.append(Player(str(splitThing[0]), str(splitThing[1]), str(splitThing[2]), str(splitThing[3]) +"/n"))
			splitThing = myFile.split("")
# close the file
		myFile.close()
		return myPlayers

keepRunning = True
while keepRunning:
	print("Welcome to Team Manager Deluxe")
	print("Start new team or open file?")
	print("Enter number to make a choice")
	print("(0)Close Program")
	print("(1)Start with a new team")
	print("(2)Open existing file")
	answer = raw_input()
#Start a new team
	if answer == "1":
		print("(0)Exit Program")
		print("(1)Add Player")
		print("(2)Print Player")
		print("(3)Save Players")
		answer = raw_input()
	#Add Player		
		if answer == "1":
			print("Okay, enter their name, age, goals, and position.")
			print("What is their name?")
			name = raw_input()
			print("What is their age?")
			age = raw_input()
			print("How many goals do they have?")
			goals = raw_input()
			print("What is their position?")
			position = raw_input()
			myPlayer = Player(name, age, goals, position)
			print("It has bee added")
			myPlayers.append(myPlayer)
	#Prints Players
		elif answer == "2":
			for p in myPlayers:
				print(p.getStats(name, age, goals))
	#Save Players
		elif answer == "3":
			filename = raw_input()
			for p in myPlayers:
				p.saveTeam(filename)
#Open Existing File
	elif answer == "2":
		print("What is the name of the file that you want to open? Enter the whole name inlcuding a .tmd at the end.")
		filename = raw_input()
		myPlayers = loadTeam(filename)
	else:
                keepRunning = False
