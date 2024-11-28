#Count how many times a specific element appears in the list.
#2
my_list = [1, 2, 2, 3, 4, 2, 5]
count = 0
for num in my_list:
    if num == 2:
        count += 1
print(count)
