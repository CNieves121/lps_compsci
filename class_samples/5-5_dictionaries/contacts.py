# makes empty list that can be added to later
myContacts = {}
# keeps the UI running
keepRunning = True
while keepRunning:
	# prints user interface so people can choose an option
	print("Welcome to Contacts.")
	print("What would you like to do?")
	print("(1)Add phone number")
	print("(2)Print all contacts")
	print("(3)Enter name and get contact")
	print("(4)Delete Contact")
	print("(5)Change Contact")
	print("(0)Close Program")
	answer = input()
	# asks users for contact name and number, then adds it to a dictionary
	if answer == 1:
		print("What's the name of the contact?")
		contactName = raw_input()
		print("What's their number?")
		contactNumber = raw_input()
		myContacts[contactName] = contactNumber
	# prints the list of contacts for user
	elif answer == 2:
		print(myContacts) 
	# asks for name and prints out their contact info
	elif answer == 3: 
		print("Who's number do you want?")
		findName = raw_input()
		print(findName + "'s number is the following: " + str(myContacts[findName]))
	# deletes contact they input
	elif answer == 4:
		print("Who's number do you want to delete?")
		delName = raw_input()
		del myContacts[delName]
	# changes contacts number
	elif answer == 5:
		print("Who's number do you want to change?")
		changeName = raw_input()
		print("What is their new number?")
		changeNumber = raw_input()
		myContacts[changeName] = changeNumber	
	# stops program
	elif answer == 0: 
		keepRunning = False
