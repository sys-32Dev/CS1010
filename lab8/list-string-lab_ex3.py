# Edwin Hui
my_char_list = ['a', 'b', 'a', 'c', 'd', 'a', 'd', 'z', 'r', 'a']
print("----------------")
print(len(my_char_list))
print("----------------")
print(my_char_list.index('d'))
# prints the index position of "d"
print("----------------")
my_char_list.insert(3, 'a')
print(my_char_list)
# inserts "a" at index 3
print("----------------")
print(len(my_char_list))
print("----------------")
print(my_char_list.count('a'))
# counts the ammount of "a" in the list
print("----------------")
count = 0
while count < len(my_char_list):
    print(my_char_list[count])
    count += 1
# prints the list one item per line
