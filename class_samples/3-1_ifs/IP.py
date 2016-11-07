
fave = 121
print("Choose a number you mortal.")
num = int(raw_input())

if fave == num:
	print("You guessed correctly. How?")
if num < fave:
	print("Nope, try something a little higher.")
if num > fave:
	print("Nope, that's way too high a number.")

if num == 11:
	print("You're getting close, this is a multiple of my number.")
