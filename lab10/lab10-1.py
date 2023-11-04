import random
my_list = ['earth', 'day', 'laptop', 'blue', 'up']

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

printhello()
count20()
print(" ")
multiply()
sort()
