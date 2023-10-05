# Prompts the user to select a burger, then sets var burger to user input
burger = int(input("Please selct a burger (1-3):"))
# if var burger is equal to 1, set var price to 3.45
if burger == 1:
    price = 3.45
# if var burger is equal to 2, set var price to 5.24
elif burger == 2:
    price = 5.24
# if var burger is equal to 3, set var price to 6.95
elif burger == 3:
    price = 6.95
# prompts the user to input if they want cheese, then sets var cheese to user input
cheese = input("Would you like cheese (Y/N):")
# if var cheese is equal to "Y", set var price to var price plus 1.23
if cheese == "Y" or "y":
    price= price + 1.23
# otherwise, keep the price the same
else:
    price = price
# prompts the user to input if they want a combo, then sets var combo to user input
combo = input("Would you like a combo (Y/N):")
# if var combo is equal to "Y" or "y", set var size to user input
if combo == "Y" or "y":
    size = input("Pick Size (S/M/L):")
    # if var size is equal to "S", set keep the price the same
    if size == "S" or "s":
        price = price
    # if var size is equal to "M", set var price to var price plus 2.76
    elif size == "M" or "m":
        price = price + 2.76
    # if var size is equal to "L", set var price to var price plus 3.89
    elif size == "L" or "l":
        price = price + 3.89
# If user does not want a combo, keep the price the same
elif combo == "N" or "n":
    price = price
# set var tax to var price multiplied by LA County tax rate
tax = price * 0.095
# set var total to var price plus var tax
total = price + tax
# prints the receipt, with menu options and choices that the user made
print("================================\n Welcome to McTofuButterBurger \n================================")
print("Menu:\n1 - McStandard (1 patty)\n2 - McGordo (2 pattys)\n3 - McChonk (3 pattys)")
print("Please select a Burger [1,2,3]", burger)
print("Add cheese to the burger? [Y/N]", cheese)
print("Would you like a combo? [Y/N]", combo)
if combo == "Y":
    print("What size combo? [S/M/L]", size)
print("--------------------------------\nYour Order:\n--------------------------------")
# prints the user's order, with the price of each item
if burger == 1:
    print("McStandard", "$3.45")
elif burger == 2:
    print("McGordo", "$5.24")
elif burger == 3:
    print("McChonk", "$6.95")
if cheese == "Y":
    print("With cheese", "$1.23")
elif cheese == "N":
    print("No cheese", "$0.00")
if combo == "Y":
    if size == "S":
        print("Small Combo", "$0.00")
    elif size == "M":
        print("Medium Combo", "$2.76")
    elif size == "L":
        print("Large Combo", "$3.89")
elif combo == "N":
    print("No Combo", "$0.00")
# Prints the price calculations
print("--------------------------------")
print("Subtotal:", "$",price)
print("Tax:", "$", tax)
print("--------------------------------")
print("Total Due:", "$",total)
print("================================")
# Thanks the user for their order
print("Thank you for your order!")