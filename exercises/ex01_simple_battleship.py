"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "760671788"

secret_location: int = int(input("Pick a secret boat location between 1 and 4: "))
if secret_location > 4: 
    print("Error! " + str(secret_location) + " too high")
    exit()
if secret_location < 1:
    print("Error! " + str(secret_location) + " too low!")
    exit()
number: int = int(input("Guess a number between 1 and 4: "))
if number > 4: 
    print("Error! " + str(number) + " too high")
    exit()
if number < 1:
    print("Error! " + str(number) + " too low!")
    exit()
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

digit_1: str = BLUE_BOX
digit_2: str = BLUE_BOX
digit_3: str = BLUE_BOX
digit_4: str = BLUE_BOX 

if number == 1:
    if number != secret_location:
        digit_1 = WHITE_BOX
    if number == secret_location:
        digit_1 = RED_BOX

if number == 2:
    if number != secret_location:
        digit_2 = WHITE_BOX
    if number == secret_location:
        digit_2 = RED_BOX

if number == 3:
    if number != secret_location:
        digit_3 = WHITE_BOX
    if number == secret_location:
        digit_3 = RED_BOX

if number == 4:
    if number != secret_location:
        digit_4 = WHITE_BOX
    if number == secret_location:
        digit_4 = RED_BOX

print(digit_1 + digit_2 + digit_3 + digit_4)

if number == secret_location:
    print("Correct! You hit the ship.")
else:
    print("Incorrect! You missed the ship.")