# List in Python

# A list is a versatile and mutable (modifiable) collection data type in Python that can hold an ordered sequence of items.
# Lists can store elements of different data types (e.g., integers, strings, floats, or even other lists)
# and are one of the most commonly used data structures in Python.

# Example: Creating a list of food items
food = ["pizza", "burger", "pasta", "hotdog"]

# Printing the entire list
print("Food List:", food)  # Output: ['pizza', 'burger', 'pasta', 'hotdog']

# Accessing individual elements by index
print("First item in the list:", food[0])  # Output: 'pizza'

# Modifying an element in the list
food[0] = "apple"
print("Updated first item:", food[0])  # Output: 'apple'

# Checking the type of the list
print("Type of food variable:", type(food))  # Output: <class 'list'>

# ===================================================================================================== #

# Mixed Data Type List
# Python lists can contain a mix of data types, including integers, strings, floats, booleans, etc.

# Example: Creating a mixed data type list
mixed_list = [1, "apple", 3.1416, True]

# Iterating through the list and printing each element with its type
print("\nMixed Data Type List:")
for item in mixed_list:
    print(item, type(item))

# Output:
# 1 <class 'int'>
# apple <class 'str'>
# 3.1416 <class 'float'>
# True <class 'bool'>
