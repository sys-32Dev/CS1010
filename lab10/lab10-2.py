# Edwin Hui
import random
accept = [4, 6, 8, 10, 12, 20]

def dice():
    print(random.randint(1, 6))
dice()
# Automatically rolls a 6 sided dice
# ----------------
def dice_1():
    return random.randint(1, 6)
print(dice_1())
# does the same as above, but with a return statement
# ----------------
def dice_2(num):
    return random.randint(1,num)
num = int(input("Enter a number: "))
print(dice_2(num))
# rools a dice with a number of sides based on user input
# ----------------
num = 0
def dice_3(num):
    if num == '':
        num = 6
    else:
        num = int(num)
    return random.randint(1,num)
num = input("Enter a number: ")
print(dice_3(num))
# rolls a dice with a number of sides based on user input
print("No input:", dice_3(''))
# Demos what happens when no input is given
# ----------------
num = 0
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
def dice_4(sides):
    num = checkSides(sides)
    return random.randint(1,num)
sides = int(input("Enter a number: "))
# prints the result of the dice roll
print(dice_4(sides))
# Demos what happens when an invalid input is given
print("Non-Valid Input:", dice_4('7'))
# ----------------
num = 0
sides = int(input("Enter a number of sides: "))
# it asks for how many times to roll now too!
rolls = int(input("Enter a number of rolls: "))
def checkSides(sides):
    if sides in accept:
        num = int(sides)
        return num
    else:
        print("Invalid number of sides, using 6 sides")
        num = 6
        return num

def dice_5(sides, rolls):
    num = checkSides(sides)
    number = [] 
    for x in range(0, rolls):
        number.append(random.randint(1,num))
    print(number)
dice_5(sides, rolls)
