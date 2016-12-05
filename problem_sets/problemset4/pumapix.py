print("Welcome to PumaPix")
print("What are your 5 favorite netfix shows?")
showlist = []
x = 1
while x <= 5:
	print("Enter a show name:")
	showlist.append(raw_input())
	x = x + 1
y = 1
while y <= 5:
	for show in showlist:
		print(str(y) + ". " + show)
		y = y + 1
print("These are the show you entered: " + str(showlist))
print("We added a couple of shows to the lsit")
showlist.append("Jessica Jones")
showlist.append("Daredevil")
z = 1 
while z <= 5:
	for show in showlist:
		showlist.sort()
		print(str(z) + ". " + show)
		z = z + 1
