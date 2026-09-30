# Game Loop
import random

# Generates one random number between 1 and 100

randomNumber = random.randint(1, 100)
print(randomNumber)
userGuess = 0

userTries = 0
userTryLimit = 3

print("Guess a number between 1 and 100!")

while (randomNumber != userGuess and userTries != userTryLimit):
    userGuess = int(input("Enter a number: "))
    if userGuess == randomNumber:
        print("You Won!")
        break;
    if userGuess < randomNumber:
        print('Too Low!')
    else:
        print('Too High!!')
    userTries = userTries + 1
    print("userTries ->", userTries)
    if userTries == userTryLimit :
        print('You Lost')