# Edwin Hui
import random
my_list = ['earth', 'day', 'laptop', 'blue', 'up']
# defining functions
def printhello():
    print("hello from my function")
def count20():
    for x in range(1,21):
        print(x, end=" ")
rn = random.randint(1, 9)
def multiply():
    print(rn * 7)
def sort():
    my_list.sort()
    print(my_list, end = " ")
print("----------------")
# prints hello from my function
printhello()
# prints 1 to 20
count20()
print(" ")
# prints random number multiplied by 7
multiply()
# prints my_list sorted
sort()
