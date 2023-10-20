# Edwin Hui
my_num_list = [3, 6, 4, 83, 2, 7, 2, 17, 4, 9, 0, 44, 2]
print("----------------")
print(my_num_list[3])
print("----------------")
my_num_list.append(8)
print(my_num_list)
# adds 8 to the end of the list, then prints the list
print("----------------")
i = 33
my_num_list.insert(4, i)
print(my_num_list)
# inserts 33 at index 4, then prints the list
print("----------------")
print(my_num_list.count(2))
print("----------------")
my_num_list.sort()
print(my_num_list)
# sorts the list, then prints the list
print("----------------")
print(len(my_num_list))
print("----------------")
my_num_list.pop()
print(my_num_list)
my_num_list.pop()
my_num_list.pop()
my_num_list.pop()
# removes the last item from the list, then prints the list, then removes 3 more
print("----------------")
print(my_num_list)
print("----------------")
print(len(my_num_list))
count = 0
while count < len(my_num_list):
    print(my_num_list[count])
    count += 1
# prints the list one item per line

