# ---------------------------
# Numeric Types
# ---------------------------
# Numeric types in Python include:
# 1. int: Represents integer values (whole numbers).
# 2. float: Represents floating-point numbers (decimal values).
# 3. complex: Represents complex numbers with a real and imaginary part.

# Example of numeric types
integer_value = 42  # Integer
float_value = 3.14  # Float
complex_value = 2 + 3j  # Complex number

# Printing the type of each numeric value
print(type(integer_value))  # Output: <class 'int'>
print(type(float_value))  # Output: <class 'float'>
print(type(complex_value))  # Output: <class 'complex'>

# ---------------------------
# String Type
# ---------------------------
# The string type (str) is used for text representation.
# Strings are sequences of characters and can be defined using single or double quotes.

# Example of string type
single_quote_string = "Hello, World!"  # Single-quoted string
double_quote_string = "Python is fun!"  # Double-quoted string

# Printing the type of each string
print(type(single_quote_string))  # Output: <class 'str'>
print(type(double_quote_string))  # Output: <class 'str'>

# String methods:
length = len(single_quote_string)  # Get the length of the string
upper_string = single_quote_string.upper()  # Convert to uppercase

# ---------------------------
# Sequence Types
# ---------------------------
# Sequence types in Python include:
# 1. list: Ordered, mutable collection of items.
# 2. tuple: Ordered, immutable collection of items.
# 3. range: Represents a sequence of numbers.

# Example of sequence types
list_example = [1, 2, 3, 4]  # List
tuple_example = (1, 2, 3, 4)  # Tuple
range_example = range(5)  # Range from 0 to 4

# Printing the type of each sequence
print(type(list_example))  # Output: <class 'list'>
print(type(tuple_example))  # Output: <class 'tuple'>
print(type(range_example))  # Output: <class 'range'>

# Accessing elements
first_element = list_example[0]  # Get the first element of the list

# ---------------------------
# Boolean Type
# ---------------------------
# The boolean type (bool) represents truth values.
# It can have two values: True and False.

# Example of boolean type
is_valid = True  # Boolean value representing True
is_complete = False  # Boolean value representing False

# Printing the type of each boolean value
print(type(is_valid))  # Output: <class 'bool'>
print(type(is_complete))  # Output: <class 'bool'>

# Boolean operations
result = is_valid and is_complete  # Logical AND operation

# ---------------------------
# None Type
# ---------------------------
# The None type represents the absence of a value or a null value.
# It is often used to signify that a variable has no value.

# Example of None type
value = None  # Variable with no value

# Checking for None and printing its type
if value is None:
    print("The variable has no value.")
print(type(value))  # Output: <class 'NoneType'>

# ---------------------------
# Set Types
# ---------------------------
# A set is an unordered collection of unique items.
# It is defined using curly braces or the set() function.

# Example of set types
set_example = {1, 2, 3, 4, 4}  # Set with unique elements
set_from_function = set([1, 2, 3])  # Create a set from a list

# Printing the type of each set
print(type(set_example))  # Output: <class 'set'>
print(type(set_from_function))  # Output: <class 'set'>

# Set operations
set_example.add(5)  # Add an element to the set
set_example.remove(2)  # Remove an element from the set

# ---------------------------
# Mapping Type
# ---------------------------
# The mapping type in Python is represented by dictionaries (dict).
# A dictionary is an unordered collection of key-value pairs.

# Example of mapping type
dict_example = {"name": "Alice", "age": 30, "city": "New York"}  # Key-value pair

# Printing the type of the dictionary
print(type(dict_example))  # Output: <class 'dict'>

# Accessing values by key
name_value = dict_example["name"]  # Get value associated with the key "name"

# Adding new key-value pairs
dict_example["job"] = "Engineer"  # Add new key-value pair
