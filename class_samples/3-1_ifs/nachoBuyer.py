print("How much do those nacho's cost?")
nacho_price = int(raw_input())
print("How much money do you have in your pocket? I'm totally not gonna rob you?")
cash = int(raw_input())
if nacho_price > cash:
	print("Sorry, no nachos for you.")
if nacho_price < cash:
	print("Have all of the nachos.")
if nacho_price == cash:
	print("I'll go ahead and take all your money now.")
