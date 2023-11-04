import random
accept = [4, 6, 8, 10, 12, 20]

def dice():
    print(random.randint(1, 6))
dice()
# ----------------
def dice_1():
    return random.randint(1, 6)
print(dice_1())
# ----------------
def dice_2(num):
    return random.randint(1,num)
num = int(input("Enter a number: "))
print(dice_2(num))
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
# ----------------
num = 0
def checkSides(sides):
    if sides in accept:
        num = int(sides)
        return num
    else:
        print("Invalid number of sides, using 6 sides")
        num = 6
        return num

def dice_4(sides):
    num = checkSides(sides)
    return random.randint(1,num)
sides = int(input("Enter a number: "))
print(dice_4(sides))
# ----------------
num = 0
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
    for x in range(0, rolls):
        return print(random.randint(1,num))
sides = int(input("Enter a number of sides: "))
rolls = int(input("Enter a number of rolls: "))
dice_5(sides, rolls)

        




