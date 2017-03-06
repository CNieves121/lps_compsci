class Player(object):
	def __init__(self, name, age, goals):
		self.name = name
		self.age = age
		self.goals = goals
	def getStats(self, name, age, goals):
		summary = "Name: " + self.name + "\n" + "Age: " + self.age + "\n" + "Goals: " + self.goals
		return summary



myPlayers = []

keepRunning = True
while keepRunning:
	print("Welcome to Team Manager Deluxe")
	print("Start new team or open file?")
	print("Enter number to makea choice")
	print("(1)Start with a new team")
	print("(2)Open existing file")
	answer = input()
	if answer == 1:i

	
	
	
	elif answer == 0:
		keepRunning = False

