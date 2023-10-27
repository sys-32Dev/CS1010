#Edwin Hui
height = 5
for i in range(height):
    for j in range(i + 1):
        print("o", end="")
    print()
# prints a triangle by adding one "o" every line until it reaches the height
print("--------------------")
height = 6
for i in range(height):
    for j in range(height - i):
        print("o", end="")
    print()
# prints a triangle by subtracting one "o" every line until it reaches the height
print("--------------------")
height = int(input("Enter the height of the triangle: "))
for i in range(height):
    for j in range(i):
        print("o", end="")
    print()
for i in range(height):
    for j in range(height - i):
        print("o", end="")
    print()
# prints a trinagle by adding one "o" every line until it reaches the user definde height, then subtracting one "o" every line 
print("--------------------")
height = int(input("Enter the height of the triangle: "))
for i in range(height):
    print(" "*(height-i-1) + "o"*(2*i+1))
# prints an equalateral triangle by printing spaces proportional to the height, then printing "o" 2 times var i + 1


