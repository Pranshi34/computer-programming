#Check if the string is Palindrome
str = input()
rev_str = str[::-1]
if str==rev_str:
  print("String is Palindrome.")
else:
  print("String is not Palindrome.")
