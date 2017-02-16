#Makes a list of the ice creams
ice_cream = ["Vanilla", "Chocolate", "Strawberry", "Slated Caramel", "Mint Chip"]
#Asks them to input a new ice cream
print("These are our ice creams: " + str(ice_cream))
print("Want to add a new flavor? Enter it now:")

ice_cream.append(raw_input())
for cream in ice_cream:
	print(cream)
