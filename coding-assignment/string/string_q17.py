#Check if a String is a Subsequence of Another
s1 = "abc"
s2 = "ahbgdc"
is_subsequence = all(c in iter(s2) for c in s1)
print(is_subsequence)  # Output: True
