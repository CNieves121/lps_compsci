#Asks for Hour
print("What hour of the day is it?")
NewYorkHours = int(raw_input())
#Asks for Minute
print("What minute of the day is it?")
NewYorkMin = int(raw_input())
#Prints Ny Time
print("It is currently " +str(NewYorkHours)+":"+str(NewYorkMin)+ " in New York.")
#Prints CA Time
CAHours = (NewYorkHours + 9) % 12
print("It is currently " +str(CAHours)+ ":"+str(NewYorkMin)+ " in California.")
