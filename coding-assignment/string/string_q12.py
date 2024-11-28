#Find the Index of the First Repeating Character.

s = "programming"
first_repeating = next((i for i, c in enumerate(s) if s.count(c) > 1), -1)
print(first_repeating) 
