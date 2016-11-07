print("How much money did you just waste?")
price = float(raw_input())
discount = float(price * .10)
sale = float(price - discount)
if price > 10.00: 
	print("You spent over $10. You're total price is going to be $" + str(sale)+"0")
