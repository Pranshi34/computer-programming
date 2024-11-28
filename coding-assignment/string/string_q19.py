#Find All Permutations of a String.
s = "abc"
n = len(s)
result = []
stack = [("", s)]
while stack:
    prefix, remaining = stack.pop()
    if len(remaining) == 0:
        result.append(prefix) 
    else:
        for i in range(len(remaining)):
            stack.append((prefix + remaining[i], remaining[:i] + remaining[i+1:]))
for perm in result:
    print(perm)
