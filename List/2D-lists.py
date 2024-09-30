# 2D Lists in Python

# A 2D list, also known as a list of lists, is essentially a list where each element is itself a list.
# This creates a two-dimensional structure, similar to a matrix or table.

# Example: Creating a 2D list
two_d_list = [
    [10, 20, 30, 40, 50],
    ["red", "green", "blue", "yellow", "purple"],
    [42, "hello", 3.14, True, None],
]

# Printing the entire 2D list
print("2D List:")
print(two_d_list)

# Accessing an entire row (list) in the 2D list
print("\nSecond row of the 2D list:")
print(two_d_list[1])  # Output: ['red', 'green', 'blue', 'yellow', 'purple']

# Accessing a specific element from a specific row
print("\nElement from the second row (index 3):")
print(two_d_list[1][3])  # Output: 'yellow'
