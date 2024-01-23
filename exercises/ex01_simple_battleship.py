"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "760671788"

secret_location = int(input("Pick a secret boat location between 1 and 4: "))

number = int(input("Guess a number between 1 and 4: "))

# Check if the input is valid (between 1 and 4)
if 1 <= secret_location <= 4:
    # If valid, exit the program without printing anything
    pass
else:
    # If invalid, print an error message depending on number
    if secret_location > 4: 
        print("Error! " + str(secret_location) + " too high")
    if secret_location < 1:
        print("Error! " + str(secret_location) + " too low!")
#do this for number(player 2) as well
if 1 <= number <= 4:
    pass
else:
    if number > 4: 
        print("Error! " + str(number) + " too high")
    if number < 1:
        print("Error! " + str(number) + " too low!")


if number == secret_location: 
    print("Correct! You hit the ship.")
else: 
    print("Incorrect! You missed the ship.")