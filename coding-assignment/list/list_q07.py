#Merge two lists into one list in alternating order.
list1 = [1, 3, 5]
list2 = [2, 4, 6]
merged_list = []
for i in range(len(list1)):
    merged_list.append(list1[i])
    merged_list.append(list2[i])
print(merged_list)
