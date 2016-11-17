lives = 3
 
while lives > 0:
    print("Choose 100 or 101.")
    choice = int(raw_input())
    if choice == 100:
        print("You win!")
    else:
        print("You lose.")
        lives = lives - 1
        print("You now have " + str(lives) + " lives.")
