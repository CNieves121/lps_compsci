print("Welcome to the haiku generator.")
print("What is the first line of your haiku?")
line1 = raw_input()
print("What is the second line of your haiku?")
line2 = raw_input()
print("What is the third line of your haiku?")
line3 = raw_input()
print("What would you like to name the file?")
title = raw_input()

my_file = open(title, "w")
my_file.write(line1 + "\n")
my_file.write(line2 + "\n")
my_file.write(line3 + "\n")

my_file.close()
