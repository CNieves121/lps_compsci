import random
myNum = random.randint(1, 1000)
guess = -1
print("I am thinking of a number between 1 and 1000")
#Debug
#print(myNum)
while guess != myNum:
	guess = int(raw_input())
	if guess > myNum:
		print("Too high, guess lower.")
	if guess < myNum:
		print("Too low, guess higher.")
	if  guess == myNum:
		print("You got it, you win!")
		break
