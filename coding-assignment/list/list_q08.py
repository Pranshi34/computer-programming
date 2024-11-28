#Check if a list contains duplicate elements.
my_list = [1, 2, 3, 4, 5, 2]
seen = set()
has_duplicates = False
for num in my_list:
    if num in seen:
        has_duplicates = True
        break
    seen.add(num)
print(has_duplicates)
