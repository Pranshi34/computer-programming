#Compress a String Using the Counts of Repeated Characters
s = "aaabbccccdaa"
compressed = ""
i = 0
while i < len(s):
    char = s[i]
    count = 1
    while i + 1 < len(s) and s[i] == s[i + 1]:
        count += 1
        i += 1
    compressed += char + (str(count) if count > 1 else "")
    i += 1
print(compressed)
