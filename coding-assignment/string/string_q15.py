#Find the Difference Between Two Strings
s1 = "abcdef"
s2 = "abcfde"
difference = "".join(set(s1) ^ set(s2))
print(difference)  

