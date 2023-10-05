# Edwin Hui
# imports random module
import random
# sets the value of rps to a random number between 0-2
rps=random.randint(0,2)
# converts the random number to either R for rock, P for paper, or S for scissors
if rps == 0:
    rps="R"
elif rps == 1:
    rps="P"
else:
    rps ="S"
# prompts the user to enter 0-2 to choose rock, paper, or scissors.
usrrps=int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors: "))
# converts user number to string
if usrrps == 0:
    usrrps="R"
elif usrrps == 1:
    usrrps="P"
else:
    usrrps ="S"
# prints the computer choice
print("computer chose:", rps)
# prints the results
if usrrps == rps:
    print("Tie")
elif usrrps == "R" and rps == "P":
    print("You lose")
elif usrrps == "R" and rps == "S":
    print("You win")
elif usrrps == "P" and rps == "R":
    print("You win")
elif usrrps == "P" and rps == "S":
    print("You lose")
elif usrrps == "S" and rps == "R":
    print("You lose")
elif usrrps == "S" and rps == "P":
    print("You win")