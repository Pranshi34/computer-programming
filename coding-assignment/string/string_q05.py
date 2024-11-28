#Check if two strings are Anagrams
str1 = input()
str2 = input()
if sorted(str1)==sorted(str2):
  print("Both strings are anagrams.")
else:
  print("Strings are not anagrams.")
