#Count Frequency of Each Character
input_string = input()
char_frequency = {}
for char in input_string:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

for char, freq in char_frequency.items():
    print(f"Character: {char}, Frequency: {freq}")
