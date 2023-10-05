# Edwin Hui
# import the random module
import random
# generate a random number between 1-10
secretNum = random.randint(1,10)
# Prompt the user to guess the number picked by the random module
print("The program has generated a random number between 1-10")
print("guess the number within 4 tries and you win.")
print("If you dont you lose!")
# sets the value of attempts var to 4
attempts = 4
# runs a while loop that will run until the attempts var is 0
while attempts > 0:
    guess = int(input("Enter your guess: "))
    # if the guess is equal to the secret number the user wins
    if guess == secretNum:
        print("You win!")
        break
    # if the guess is higher than the number the user is told that and a attempt is removed 
    elif guess > secretNum:
        print("Number too high!")
        attempts -= 1
        # if the guess is lower than the number the user is told that and a attempt is removed 
    elif guess < secretNum:
        print("Number too low!")
        attempts -= 1
    if attempts == 0:
        # if the attempts var is 0 the user loses and the number is printed
        print("You lose!, the number was:", secretNum)
        break
