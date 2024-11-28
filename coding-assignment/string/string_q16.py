#Extract the Numeric Part of a String
s = "Price: 12345 USD"
numeric_part = "".join([c for c in s if c.isdigit()])
print(numeric_part) 
