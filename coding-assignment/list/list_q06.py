#Find the index of the first occurrence of a given element.
my_list = [5, 3, 8, 1, 9, 2]
element = 8
index = -1
for i in range(len(my_list)):
    if my_list[i] == element:
        index = i
        break
print(index)
