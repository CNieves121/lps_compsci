count = 2
def isPrime(myNum):
	for x in range(1,11):
		if x % count == 0:
			return False
		else: 
			return True

myFile = open("numbersPrime.txt", "w")
for n in range(2, 11):
	if isPrime(n):
		myFile.write(str(n) + "/n")
myFile.close()

