# Find the common elements between two tuples.

def common_elements(tup1, tup2):
    return tuple(x for x in tup1 if x in tup2)

tup1 = (1, 2, 3, 4)
tup2 = (3, 4, 5, 6)
common = common_elements(tup1, tup2)
print(common)
