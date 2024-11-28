#Replace all occurrences of a specific element in a list.
my_list = [1, 2, 3, 2, 4]
old_value = 2
new_value = 9
for i in range(len(my_list)):
    if my_list[i] == old_value:
        my_list[i] = new_value
print(my_list)
