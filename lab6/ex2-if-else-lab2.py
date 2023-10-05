# Edwin Hui
# Prints a list of animals that are avalible to be chosen.
print("Octopus, Fish, Tarantula, Snake")
# Asks the user to choose one of the animals listed.
userchoice=input("Please enter one of the animals listed: ")
print("the program will now guess your animal")
# Program asks the susers questions to determine what animal they chose.
choice1=input("Does your animal live in the ocean? (Y/N)")
if choice1=="Y":
    choice2=input("Does your animal have 8 legs? (Y/N)")
    if choice2=="Y":
        print("Your animal is an Octopus")
    else:
        print("Your animal is a Fish")
else:
    choice3=input("Does your animal have 8 legs? (Y/N)")
    if choice3=="Y":
        print("Your animal is a Tarantula")
    else:
        print("Your animal is a Snake")
