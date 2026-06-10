#this is a guessing game
##the computer generates a random number - there must exist a function and a variable
##accept user input as a guess - so your guess is a variable 
##function that compares your variable to the random number
#if not same, returns sorry you're wrong, and exits

#create random number
import random

randNum = random.randrange(1,10)

#take user input
print("Guess the lucky number!")
userGuess = input()

#convert string input (userGuess) to number 
userGuess_int = int(userGuess)
#compare both numbers
if randNum != userGuess_int:
    print("You did not guess the lucky number...")
else:
    print("You guessed the lucky number!!")

