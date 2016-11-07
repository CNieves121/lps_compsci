print("How many donuts will there be at the party?")
donuts = int(raw_input())

print("How many people will come to the party?")
people = int(raw_input())

print("Our party has " + str(people) + " people and " + str(donuts) + " donuts.")

each = donuts // people
print("Each person at the party will get " + str(each)  + " donuts.")
