#Interleave two lists of unequal length.
list1 = [1, 3, 5]
list2 = [2, 4]
result = []
min_len = min(len(list1), len(list2))
for i in range(min_len):
    result.append(list1[i])
    result.append(list2[i])
result.extend(list1[min_len:])
result.extend(list2[min_len:])
print(result)
