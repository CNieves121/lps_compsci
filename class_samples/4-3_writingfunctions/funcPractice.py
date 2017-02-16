a = .65
b = 2
c = 7
d = 10
"""
# 1
# the argument x must be a number
# returns x to the 3rd power
def cube(x):
        return x ** 3
# test number 1
print("1 -------- Cube b, c, d:")
print(cube(b))
print(cube(c))
print(cube(d))
# 2
# the argument x must be a number
# returns x as a string and as a percentage, converted to an integer %
# for example, if x is .252, returns "25%"
def pct_string(x):
        return str(x * 100) + "%" 

# test number 2
print("#2 ---------- Show a and a+b as percentages:")
print(pct_string(a))
print(pct_string(a+b))

# 3
# the argument myStr must be a string
# does not return anything but prints myStr three times on separate lines
def print_thrice(myStr):
        print(myStr)
	print(myStr)
	print(myStr)

# test number 3
print("3 --------- Print b three times, then d three times.")
print_thrice(b)
print_thrice(d)

# 4
# the arguments x and y must be numbers
# returns the average of the two numbers as a float
# hint - you'll need to divide by 2.0
def my_avg(x, y):
        return (float(x) + float(y)) / float(2)
# test number 4
print("#4 --------- Average b and c, then b and d.")
print(my_avg(b,c))
print(my_avg(b,d))
"""


print("Tester")
# DON'T TOUCH THIS CODE
# Test the function implementations
print("**************Results****************")
p = 2
q = 5
r = .25

"""
# number 1
if cube(p) == 8 and cube(q) == 125:
  print("#1 passes")
else:
  print("#1 fails")
 
# number 2
if pct_string(r) == "25.0%":
  print("#2 passes")
else:
  print("#2 fails")
 
# number 3
print("#3 passes if the next three lines are all \"bird\"")
print_thrice("bird")

# number 4
print(my_avg(p, q))
print(my_avg(p, 2*q))
if my_avg(p, q) == 3.5 and my_avg(p, 2*q) == 6:
  print("#4 passes")
else:
  print("#4 fails")
"""
#Challenge 
def my_max(myList):
        myList.reverse()
	return(myList[0])
# challenge
if my_max([p]) != None:
        l = [1, 9, -4, 130]
        if my_max(l) == 130:
                print("Nice work on the challenge, it passes!")
        else:
                print("Good work attempting the challenge, but your function fails.")
