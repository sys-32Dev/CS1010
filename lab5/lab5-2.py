# Asks user for input of an intger, then sets var number to user input
number = int(input("Enter a number: "))
# if var number is greater than 42, print "your number is higher"
if number > 42:
    print("your number is higher")
# if number is less than 42, print "your number is lower"
elif number < 42:
    print("your number is lower")
# else, print "you entered 42"
else:
    print("you entered 42")