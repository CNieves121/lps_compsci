bacteria_population = 1
minutes = 0
 
while bacteria_population < 5000000:
        print("After " + str(minutes) + " minutes, there are " + str(bacteria_population) + " bacteria in the sink.")
        print("No need to disinfect the sink yet.")
        bacteria_population = bacteria_population * 2
        minutes = minutes + 1
 
print("After " + str(minutes) + " minutes, there are " + str(bacteria_population) + " bacteria in the sink.")
print("You shoud use some Clorox on the sink now.")



"""
account_balance = 1000
 
withdrawal = 50
 
while account_balance > 0:
        print("Ok, your withdrawal has been made.")
	account_balance = account_balance - withdrawal
        print("Your balance is now $" + str(account_balance) + ".")
"""
