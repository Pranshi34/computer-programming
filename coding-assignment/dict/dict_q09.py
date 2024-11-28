# Write a Python program to create a dictionary from a string.


input_string = "hello world"
char_count = {}
for char in input_string:
    if char in char_count:
        char_count[char] += 1  
    else:
        char_count[char] = 1  
print("Character Frequency Dictionary:", char_count)
