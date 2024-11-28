#Move All Zeros to the End of a List
lst = [0, 1, 9, 0, 4, 0, 2, 5, 0]
non_zero_index = 0
for i in range(len(lst)):
    if lst[i] != 0:
        lst[non_zero_index], lst[i] = lst[i], lst[non_zero_index]
        non_zero_index += 1
print(lst)
