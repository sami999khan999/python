# ---------------------------
# String Indexing
# ---------------------------
# In Python, strings are ordered sequences of characters.
# Each character in the string has an index, which can be used to access individual characters.
# Indexing starts from 0 for the first character and goes up to n-1, where n is the length of the string.

example_string = "Python"

# Accessing individual characters using indexing:
first_char = example_string[0]  # First character: 'P'
second_char = example_string[1]  # Second character: 'y'

print(f"First character: {first_char}")  # Output: P
print(f"Second character: {second_char}")  # Output: y


# ---------------------------
# Positive Indexing
# ---------------------------
# Positive indexing starts from 0 for the first character.
# It allows you to access characters from the beginning of the string.

# Example string: "Python"
# P = index 0
# y = index 1
# t = index 2
# h = index 3
# o = index 4
# n = index 5

third_char = example_string[2]  # Character at index 2: 't'
print(f"Character at index 2: {third_char}")  # Output: t


# ---------------------------
# Negative Indexing
# ---------------------------
# Negative indexing allows you to access characters from the end of the string.
# The last character has an index of -1, the second last character has an index of -2, and so on.

# Example string: "Python"
# n = index -1
# o = index -2
# h = index -3
# t = index -4
# y = index -5
# P = index -6

last_char = example_string[-1]  # Last character: 'n'
second_last_char = example_string[-2]  # Second last character: 'o'

print(f"Last character: {last_char}")  # Output: n
print(f"Second last character: {second_last_char}")  # Output: o


# ---------------------------
# String Slicing
# ---------------------------
# String slicing allows you to extract a substring from a string.
# The syntax for slicing is: string[start:end] where 'start' is the index to begin the slice,
# and 'end' is the index where the slice stops (but the character at the 'end' index is not included).

# Example string: "Python"
substring = example_string[0:3]  # Slicing from index 0 to 3 (but not including 3)
print(f"Substring (0:3): {substring}")  # Output: Pyt

# Omitting the start or end index will take everything from the beginning or up to the end:
substring_from_start = example_string[
    :4
]  # Slicing from the start to index 4 (not including 4)
substring_to_end = example_string[3:]  # Slicing from index 3 to the end of the string

print(f"Substring from start: {substring_from_start}")  # Output: Pyth
print(f"Substring to end: {substring_to_end}")  # Output: hon


# ---------------------------
# String Concatenation
# ---------------------------
# String concatenation means combining multiple strings together using the + operator.

string1 = "Hello"
string2 = "World"

concatenated_string = string1 + " " + string2  # Concatenating with a space in between
print(f"Concatenated String: {concatenated_string}")  # Output: Hello World


# ---------------------------
# String Repetition
# ---------------------------
# You can repeat a string multiple times using the * operator.

string_to_repeat = "Python"

repeated_string = string_to_repeat * 3  # Repeat the string 3 times
print(f"Repeated String: {repeated_string}")  # Output: PythonPythonPython
