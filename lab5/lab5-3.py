# asks user for a numeric grade inputm then sets var numbergrade to user input
numbergrade = int(input("Enter a number grade from 0-100: "))
# if var numbergrade is greater than or equal to 90, print "You have an A"
if numbergrade >= 90 and numbergrade <= 100:
    print("You have an A")
# if var numbergrade is greater than or equal to 80, print "You have a B"
elif numbergrade >= 80 and numbergrade < 90:
    print("You have a B")
# if var numbergrade is greater than or equal to 70, print "You have a C"
elif numbergrade >= 70 and numbergrade < 80:
    print("You have a C")
# if var numbergrade is less than 70, print "You got No Credit"
else:
    print("You got No Credit")