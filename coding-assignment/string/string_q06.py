#Find the longest word in this string without using functions
input_string = input()
words = input_string.split()
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print("The longest word is:", longest_word)
