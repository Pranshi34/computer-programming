# Write a Python program to remove spaces from dictionary keys.


data = {'first name': 'John', 'last name': 'Doe', 'age': 30, 'country of birth': 'USA'}
data_no_spaces = {key.replace(' ', ''): value for key, value in data.items()}
print("Dictionary with spaces removed from keys:", data_no_spaces)
