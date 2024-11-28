# Remove an element from a tuple.

def remove_element(tup, value):
    return tuple(x for x in tup if x != value)

tup = (1, 2, 3, 4, 3, 5)
new_tup = remove_element(tup, 3)
print(new_tup)  
