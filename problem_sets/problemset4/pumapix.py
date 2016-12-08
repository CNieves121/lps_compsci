print("Welcome to PumaPix")
print("What are your 5 favorite netfix shows?")
showlist = []
x = 1
while x <= 100000000:
	print("Enter a show name:")
	addshow = raw_input()
	showlist.append(addshow)
	x = x + 1
	if addshow == "done":
		showlist.remove("done")
		break
y = 1
while y <= 5:
	for show in showlist:
		print(str(y) + ". " + show)
		y = y + 1
print("These are the show you entered: " + str(showlist))
print("We added a couple of shows to the lsit")
showlist.append("Jessica Jones")
showlist.append("Daredevil")
showlist.sort()
z = 1 
while z <= 5:
	for show in showlist:
		print(str(z) + ". " + show)
		z = z + 1
