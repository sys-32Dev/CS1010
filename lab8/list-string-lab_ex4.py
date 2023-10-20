# Edwin Hui
num_list = [34, 42, 99, 1301, 1, 78, 314, 818, 777]
print(num_list)
print("----------------")
add = 0
count = 0
while count < len(num_list):
    print(num_list[count], end = " ")
    add = add + num_list[count]
    count += 1
# prints the list all in one line, while adding the list items together
print()
print("total:", add)
num_list.sort()
print("largest number:", num_list[8])
# sorts the list, then prints last item in the list (which is the largest number)
print("----------------")
num_list = [3, 7, 999, 1981, 1066, -4086, 33]
print(num_list)
add = 0
count = 0
while count < len(num_list):
    print(num_list[count], end = " ")
    add = add + num_list[count]
    count += 1
print()
print("total:", add)
num_list.sort()
print("largest number:", num_list[6])
# repeats above but for a different list
