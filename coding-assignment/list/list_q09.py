#Rotate a list by n positions to the right.
my_list = [1, 2, 3, 4, 5]
n = 2
rotated_list = my_list[-n:] + my_list[:-n]
print(rotated_list)
