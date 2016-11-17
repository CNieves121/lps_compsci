print("What number do you want the multiples for?")
ognum = int(raw_input())
multiple = 0
number = 1
while number <= 1000:
	number = ognum * multiple
	multiple = multiple + 1
	print(str(ognum) + " times " + str(multiple - 1) + " is equal to " + str(number))
	if number  >= 1000:
		print("These are the multiples of the number " + str(ognum))
		break
