#Replace Digits with Their Word Equivalents
s = "I have 2 apples and 3 bananas"
digit_map = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three'}
replaced = "".join([digit_map[c] if c in digit_map else c for c in s])
print(replaced)  # Output: "I have two apples and three bananas"
