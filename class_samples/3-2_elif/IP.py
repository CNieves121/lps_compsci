print("How far away do you live from Richmond State?")
miles = int(raw_input())

print("What is your GPA?")
gpa = float(raw_input())

if miles <= 30 and gpa >= 2.0:
	print("Congrats you're in.")
elif miles <= 30 and gpa < 2.0: 
	print("Sorry your gpa is not high enough.")
else:
	print("What is your ACT score?")
	act = int(raw_input())
	if miles >= 30 and gpa >= 2.5 and act >= 18:
		print("You're in.")

	else:
		gpachange = 2.5 - gpa
		actchange = 18 - act
		print("You're out")
		print("You'll need to raise you're gpa by " + str(gpachange))
		print("You'll need to raise your act score by " + str(actchange))


