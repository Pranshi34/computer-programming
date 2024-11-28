#  Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.


data = {'1': 'abc', '2': 'de', '3': 'fg'}
values = list(data.values())
for char1 in values[0]:
    for char2 in values[1]:
        for char3 in values[2]:
            print(char1 + char2 + char3)
