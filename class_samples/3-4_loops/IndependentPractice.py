"""
x = 1
 
while x <= 10:
    print(x)
    x = x + 1
"""

x=1
print("Can you guess my favorite number?")
x = int(raw_input())
while x != 14:	
	if x != 14:
		print("Nope, try again.")
		x = int(raw_input())
		if x == 14:
			print("Yup")
"""
x=int(raw_input())
while x > 0:
	print(range(1,1000000))	

"""
