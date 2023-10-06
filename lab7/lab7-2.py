# Edwin Hui
loop = 0
result = 0
while loop >= 0:
    add = loop + 1
    print(result, "+", add, "=", result + add)
    result = result + add
    loop = loop + 1
    if loop == 100:
        break