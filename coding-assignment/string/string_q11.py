#Check if Two Strings are Rotations of Each Other
s1 = "abcd"
s2 = "cdab"
is_rotation = len(s1) == len(s2) and s2 in s1 + s1
print(is_rotation)  
