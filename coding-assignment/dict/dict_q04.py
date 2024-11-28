 # Write a Python script to sort (ascending and descending) a dictionary by value.

data = {'a': 3, 'b': 1, 'c': 2, 'd': 4}
sorted_asc = dict(sorted(data.items(), key=lambda item: item[1]))
sorted_desc = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
print("Original Dictionary:", data)
print("Sorted Dictionary (Ascending):", sorted_asc)
print("Sorted Dictionary (Descending):", sorted_desc)
