# put this line at the start of your program
# to make the functions of this package available
import random

#Asks user for their name as well as their atributes
print("What is your name traveler?")
name = raw_input()
print("How strong are you " + name + "?(Enter a value of 1-10) Note that you can only have a total of 15 points.")
strength = int(raw_input())
print("How lucky are you " + name + "?(Enter a value of 1-10)")
luck = int(raw_input())
print("How healthy are you " + name + "? (Enter a value of 1-10)")
health = int(raw_input())
#If their luck is high enough then they have a better chance to get a higher number for an encounter.
if luck >= 5: 
	realluck = random.randint(50,100)
else:
	realluck = random.randint(5,100)
#Makes sure that their points are correctly attributed, if not then it sets them to a default of 5 each
if health + luck + strength > 15:
	strength = 5
	luck = 5
	health = 5
	print("That doesn't make sense, I'm going to assume that your luck, strength, and health are all 5.")
else:
	print("That seems about right just from the look of ya. So your strength is: " + str(strength) + " your luck is: " + str(luck) + " and your health is: " + str(health))

#Sets uf the fork in the road
print("There is a fork in the road. Which way are you going to go traveler, right, left or straight ahead?")
direction = raw_input()

#If they go right and they have a strength of 6 or higher then win, if not they lose
if direction == "right" and  strength >= 6:
	print("You have arrived at Hogwart an found that the Womping Whillow is in the way. Luckily you were strong enough to survive its brutish attacks and  you find your way into Hogwarts anyways. Congradulations, You're a wizard " + name)
elif direction == "right" and strength < 6:
	print("You arrive at Hogwarts to find the Womping Whillow in your way. Sadly, you don't have the strength to overcome its attacks and perish where you stand. Not to mention that it disposes of your body where you will never be found... Good luck on the next try traveler.")

#If they go left and they have a health of 9 or higher they win, if not they have a health between 4 and 8 they get sent to the wall, if they get lower than a 4 they lose.
elif direction == "left" and health >= 9:
	print("You have found your way to the land of Westeros, more specifically Winterfell. You are bombarded by a volley of arrows, but luckily you have the health to endure the attack. Suddenly you see a man walk through a gate to question you. He admires your resistance and decides to take you in as a warrior. I'd call that winning.")
elif direction == "left" and (health >= 4 or health < 9):
	print("You have found your way to the land of Westeros, more specifically Winterfell. You are bombarded by a volley of arrows and just barely survive. As you fade out of consciousness you see people coming out to help you. When you awake there is a doctor helping you with your injuries. He tells you that you are going to be sent to The Wall. You don't lose, but you sure as hell don't win.")
elif direction == "left" and health < 4:
	print("You seem to have found your way to Westeros, more specifically Winterfell. You are bombarded by a volley of arrows and immediately fall due to your low health. As you drift away you see people come to your aid, but it is too late for that.")

#If they go straight ahead and have luck 5 or higher they have a higher chance to win this encounter. If the number generated is high enough they win, if not they lose.
elif direction == "straight ahead" and realluck >= 70:
	print("You seem to have found your way into Skyrim. You see guards running towards you an you begin to run, luckily for you, a dragon comes out of nowhere and distracts the guards. You get away safely and find your way to the home of the Thieves Guild where you spend the rest of your life.")
elif direction == "straight ahead" and realluck <70:
	print("You seem to have found your way into Skyrim. You see guards running towards you and being to run. Sadly you don't run fast enough and they imprison you.")
