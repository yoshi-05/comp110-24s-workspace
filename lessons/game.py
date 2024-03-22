"""Number Guessing Game"""

from random import randint

SECRET: int = randint(1,10)
correct: bool = False



#while not correct: # correct == False
while correct == False: 
    guess: int = int(input("Guess a number: "))
    if guess > 10:
        print("Error, too high!")
    if guess < 1: 
        print("Error, too low!")   
    if guess == SECRET:
        print(f"You got it right! {guess} is the secret number!")
        correct = True
    else:
        print("Try again!")