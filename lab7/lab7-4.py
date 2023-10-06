# Edwin Hui
loop = 0
while loop < 6:
    print("#" * loop)
    loop += 1
print("----------------------------------")
loop = input("Enter number of lines: ")
nbr = int(loop)
loop = 0
while loop <= nbr:
    chara = 0
    print("")
    while chara < loop:
        print("#", end="")
        chara += 1
    loop += 1