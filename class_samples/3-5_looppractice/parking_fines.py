months = 0 
ticket = 60

while ticket > 0:
	print("Have you paid you're ticket? yes/no")
	response = raw_input()
	if response == "yes":
		ticket = 0
	else:
		ticket = ticket * 2
		print("Okay, you're ticket is now " +  str(ticket))
