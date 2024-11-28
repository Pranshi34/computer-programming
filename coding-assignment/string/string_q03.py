#Count vowels in a string
str = input()
vowels = "A,E,I,O,U,a,e,i,o,u"
count = 0
for i in range(len(str)):
  if str[i] in vowels:
    count+=1
print(count)
