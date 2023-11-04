# Edwin Hui
import random
accept = [4, 6, 8, 10, 12, 20]
number = []
# checks if the number of sides is valid, if not, sets it to 6
def checkSides(sides):
    if sides in accept:
        num = int(sides)
        return num
    else:
        print("Invalid number of sides, using 6 sides")
        num = 6
        return num
# rolls a dice with a number of sides based on user input
def dice(sides, rolls):
    num = checkSides(sides)
    number = [] 
    for x in range(0, rolls):
        number.append(random.randint(1,num))
    return number
# asks for how many sides and how many times to roll
def ask():
    global sides
    global rolls
    sides = int(input("Enter a number of sides: "))
    rolls = int(input("Enter a number of rolls: "))
    return sides, rolls
# loops the dice rolling
def loop():
    global sides
    global rolls
    global number
    print("--------------------------------")
    number = dice(sides, rolls)
    while len(number) > 0:
        print(number[0], end="       ")
        number.pop(0)
    print("\n--------------------------------")
    pram = input("Press Enter to re-roll, q to quit, or n to set new parameters->")
    if pram == "q":
        # quits the program
        print("Goodbye")
    elif pram == "":
        # rerolls with the same parameters
        loop()
    elif pram == "n":
        # lets you set new parameters
        sides = int(input("Enter a number of sides: "))
        rolls = int(input("Enter a number of rolls: "))
        loop()
ask()
loop()