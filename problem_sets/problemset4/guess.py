import random
myNum = random.randint(1, 1000)
guess = -1
points = 0
print("I am thinking of a number between 1 and 1000")
#Debug
#print(myNum)
while guess != myNum:
	guess = int(raw_input())
	points = points + 1
	if guess > myNum:
		print("Too high, guess lower.")
	if guess < myNum:
		print("Too low, guess higher.")
	if  guess == myNum:
		print("You got it, you win!")
		break
print("It took you " + str(points) + " guesses to guess the correct number.")
