#Find the First Non-Repeating Character
input_string = input()
char_frequency = {}
for char in input_string:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
first_non_repeating = None
for char in input_string:
    if char_frequency[char] == 1:
        first_non_repeating = char
        break
if first_non_repeating:
    print("First non-repeating character:", first_non_repeating)
else:
    print("No non-repeating character found.")
