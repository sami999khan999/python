name = "samikhan"

# lenght

# The len() function in Python is used to determine the length of various data structures, such as strings, lists, tuples, dictionaries, and more. It returns the number of items in the object.
print(len(name))

# ===================================================================================================== #

# find

# The find() method in Python is used to search for a substring within a string. It returns the lowest index of the substring if it is found. If the substring is not found, it returns -1.
print(name.find("s"))
print(name.find("k"))

# ===================================================================================================== #

# capitalize

# The capitalize() method in Python is used to convert the first character of a string to uppercase and the rest of the characters to lowercase.

print(name.capitalize())

# ===================================================================================================== #

# uppder and lowercase

# In Python, you can use the upper() and lower() methods to convert a string to uppercase and lowercase, respectively.

print(name.upper())
print(name.lower())

# ===================================================================================================== #

# isdigit

# The isdigit() method in Python is used to check if all the characters in a string are digits. If the string contains only digit characters, it returns True; otherwise, it returns False.

print(name.isdigit())

# ===================================================================================================== #

# isalpha

# The isalpha() method in Python is used to check if all the characters in a string are alphabetic letters. If the string contains only alphabetic characters (and is non-empty), it returns True; otherwise, it returns False.

print(name.isalpha())

# ===================================================================================================== #

# count

# The count() method in Python is used to count the number of occurrences of a substring within a string. It returns an integer representing the number of times the substring appears.
print(name.count("a"))

# ===================================================================================================== #

# replace

# The replace() method in Python is used to replace occurrences of a specified substring with another substring. It returns a new string with all (or specified number of) replacements.
print(name.replace("a", "b"))

# ===================================================================================================== #

print(name*10)