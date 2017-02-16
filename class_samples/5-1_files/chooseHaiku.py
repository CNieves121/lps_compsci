#asks user to unput which haiku to print
print("What Haiku would you like to read?")
print("(3) A haiku about thing 3")
print("(4) A haiku aobut thing 4")
answer = int(raw_input())
#prints out one of two haiku depending on suer input
if answer == 3:
	my_file = open("haiku3.txt", "r")
	print my_file.read()
	my_file.close()
elif answer ==4:
	my_file = open("haiku4.txt", "r")
        print my_file.read()
        my_file.close()
