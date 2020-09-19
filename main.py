import random 

print("*****WELCOME TO THE GUESSING GAME*****")

#### Project Planning
# 1) Number randomizer for computer
# 2) Loop for replaying
# 3) Conditonals to play again or evaluate players number vs. computers number
# 4) Provide user input for players number

print("I AM COMPUTER. GUESS MY NUMBER")

computerNum = random.randint(0,20)
print(computerNum)

#state variables
win = False
still_playing = True
tries = 5

while still_playing == True:
    while tries > 0:
        print()
        playerNum = int(input("Enter a number between 0-20: "))

        if playerNum > computerNum:
            print("Your number is too big!")
            tries -= 1
            print("You have " + str(tries) + " tries left.")
        elif playerNum < computerNum:
            print("Your number is too small.")
            tries -= 1
            print("You have " + str(tries) + " tries left.")
        else:
            print("You guessed the correct number!")
            win = True
            break
    if win == True:
        print("Congratulations! You won at " + str(6-tries) + " tries")
    else:
        print("No more tries")
        print("The number was: " + str(computerNum))

    answer = input("Do you want to play again? Y or N: ")

    #create a conditional to assess what happens if the player entered Y or N.
      
    if answer.upper() == "N":
        print("Okay! byeeee")
        still_playing = False
    else:
        win = False
        tries = 5
        computerNum = random.randint(0, 20)
