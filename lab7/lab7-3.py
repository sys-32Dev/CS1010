# Edwin Hui
usr = input("enter a number or q to quit: ")
if usr == "q":
    print("you have no total")
else:
    print("your subtotal is", usr)
    while usr != "q":
        usr2 = input("enter a number or q to quit: ")
        if usr2 == "q":
            print("your grand total is", subtotal)
            break
        subtotal = int(usr) + int(usr2)
        print("your subtotal is", subtotal)
        usr = subtotal

