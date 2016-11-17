print("What number do you want the multiples for?")
ognum = int(raw_input())
print("How high would you like this to go?")
ceiling = int(raw_input())
multiple = 0
number = 1
while number <= ceiling:
	number = ognum * multiple
	multiple = multiple + 1
	print(str(ognum) + " times " + str(multiple - 1) + " is equal to " + str(number))
	if number  >= (ceiling + 1):
		print("These are the multiples of the number " + str(ognum))
		print("There are " + str(multiple) + " integer multiples of " + str(ognum) + " that are less than " + str(ceiling))
		break
