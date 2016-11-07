print("How old are you?")
age = int(raw_input())

print("What's your GPA?")
gpa = float(raw_input())

if gpa > 3.0 and age > 16:
	print("Congrats, Welcome to College!")
if gpa <= 3.0 and age <= 16: 
	print("You suck, get better nurd!")
else:
	print("")
