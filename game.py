#Number-Guessing-Game

#This is a guessing game, where the computer generates a random number and accepts user input as a guess
# If not same, returns sorry you're wrong, and exits

#create random number
import random

randNum = random.randint(0,1000)
#take user input
print("Guess the lucky number!")
userGuess = input()

#convert string input (userGuess) to number 
userGuess_int = int(userGuess)

#define a hint function- game tells you whether userGuess is too high or too low
def userHint(real, guess):
    if real < guess:
        print("Guess is too high")
    elif real > guess:
        print("Guess is too low")
    else:
        pass



#create a loop giving you a fixed amount of attempts - while loop 4 iterations 
x = 1
while x < 5:
    #compare both numbers
    if randNum != userGuess_int:
        userHint(randNum, userGuess_int)
        print("You did not guess the lucky number. Guess again...")
        userGuess_int = int(input())   ##wrapping function in a function
    else:
        print("You guessed the lucky number!!")
        break
    x += 1

print("Game over. Would you like to play again?")