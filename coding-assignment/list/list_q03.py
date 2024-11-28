#Find the largest and smallest element in a list.
my_list = [5, 3, 8, 1, 9, 2]
largest = my_list[0]
smallest = my_list[0]

for num in my_list:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)
