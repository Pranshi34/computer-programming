#Find all the unique elements in a list.
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_elements = []
for num in my_list:
    if num not in unique_elements:
        unique_elements.append(num)
print(unique_elements)
