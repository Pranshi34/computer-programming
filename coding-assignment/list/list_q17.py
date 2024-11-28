# Python program to find N largest element from given list of integers.

l = [1000,298,3579,100,200,-45,900]
n = 4
l.sort()
arr = []
while n:
	arr.append(l[-n])
	n -= 1
print(arr)
