# Edwin Hui
import time
import random

print("this")
time.sleep(1)
print("is")
time.sleep(2)
print("a")
time.sleep(4)
print("test")
time.sleep(3)
print("message")
print("----------------------------------")
print(time.time())
time.sleep(0.5)
print(time.time())
time.sleep(1)
print(time.time())
print("----------------------------------")
loops = 9
while loops > -1:
    print(10-loops)
    loops = loops - 1
print("----------------------------------")
loops = 9
while loops > -1:
    print(10-loops, end=" - ")
    loops = loops - 1
print("----------------------------------")
loops = 4
while loops > -1:
    print(5-loops)
    loops = loops - 1
    time.sleep(0.5)
print("----------------------------------")
loops = 10
while loops <= 20:
    print(loops)
    loops = loops + 2
    if loops == 22:
        break
print("----------------------------------")
loops = 20
while loops <= 20:
    print(loops)
    loops = loops - 3
    if loops <= 0:
        break
print("----------------------------------")
loops = 10
while loops > 0:
    print(random.randint(1,100), end=" ")
    loops = loops - 1
print("----------------------------------")
nbr = int(input("Enter a number greater than 100: "))
while nbr <= 100:
    print("Number too low!")
    nbr = int(input("Enter a number greater than 100: "))
    if nbr > 100:
        print("Number is greater than 100, thank you!")
        break
print("----------------------------------")
