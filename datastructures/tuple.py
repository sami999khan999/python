# ---------------------------
# Creating and Manipulating Tuples
# ---------------------------
# A tuple in Python is an ordered collection of items, similar to a list.
# However, tuples are immutable, meaning once created, their content cannot be changed.

# Example: Creating a tuple
fruits = ("apple", "banana", "cherry")
print(fruits)  # Output: ('apple', 'banana', 'cherry')

# Explanation:
# - The tuple `fruits` contains three elements.
# - Tuples are created using parentheses `()`, unlike lists which use square brackets `[]`.

# Accessing tuple elements by index:
first_fruit = fruits[0]  # Accessing the first item
last_fruit = fruits[-1]  # Accessing the last item
print(first_fruit)  # Output: apple
print(last_fruit)  # Output: cherry

# ---------------------------
# Tuple Methods: count() and index()
# ---------------------------

# Tuples have limited methods because they are immutable.
# Two of the most commonly used methods are `count()` and `index()`.

# ---------------------------
# Using count() to count occurrences of an item
# ---------------------------
# The count() method returns the number of times a value appears in a tuple.

# Example: Counting the occurrence of an item in a tuple
numbers = (1, 2, 3, 1, 1, 4, 5)
occurrences_of_one = numbers.count(1)
print(occurrences_of_one)  # Output: 3

# Explanation:
# - The value `1` appears 3 times in the `numbers` tuple.


# ---------------------------
# Using index() to find the first occurrence of an item
# ---------------------------
# The index() method returns the index of the first occurrence of a value.

# Example: Finding the index of an item in a tuple
index_of_banana = fruits.index("banana")
print(index_of_banana)  # Output: 1

# Explanation:
# - The value "banana" is located at index 1 in the `fruits` tuple.


# ---------------------------
# Tuple Slicing
# ---------------------------
# Just like lists, tuples support slicing to access portions of the tuple.
# Syntax: tuple[start:end:step] (start is inclusive, end is exclusive)

# Example: Slicing a tuple
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
slice_of_tuple = numbers[2:5]  # Get items from index 2 to 4
print(slice_of_tuple)  # Output: (2, 3, 4)

# Example: Slicing with a step
every_other_number = numbers[::2]  # Get every second item (step=2)
print(every_other_number)  # Output: (0, 2, 4, 6, 8)

# Explanation:
# - The slice notation allows you to access portions of the tuple.
# - You can also define a step value to skip elements, as shown with `::2`.


# ---------------------------
# Looping Through Tuples
# ---------------------------
# You can loop through a tuple using a for loop, just like with lists.

# Example: Looping through a tuple
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry

# Explanation:
# - The for loop iterates over the `fruits` tuple, and each element is printed.


# ---------------------------
# Use case: Storing coordinates as tuples
# ---------------------------
# Tuples are useful for storing fixed sets of data that shouldn't change, such as coordinates.

# Example: Using tuples to represent coordinates
coordinate = (10.0, 20.0)

# Accessing coordinate values
x = coordinate[0]
y = coordinate[1]
print(f"X: {x}, Y: {y}")  # Output: X: 10.0, Y: 20.0

# Explanation:
# - The tuple `coordinate` represents a point in a 2D space.
# - Tuples are often used for this type of data because they ensure immutability (the coordinates cannot be accidentally changed).


# ---------------------------
# Use case: Returning multiple values from a function
# ---------------------------
# Functions in Python can return multiple values as a tuple.


# Example: Returning a tuple from a function
def get_min_max(numbers):
    return min(numbers), max(numbers)  # Returning a tuple of (min, max)


# Calling the function
result = get_min_max([1, 2, 3, 4, 5])
print(result)  # Output: (1, 5)

# Explanation:
# - The function `get_min_max` returns the minimum and maximum values as a tuple.
# - This is a common pattern when functions need to return multiple values.


# ---------------------------
# Use case: Tuple Unpacking
# ---------------------------
# You can unpack a tuple into separate variables.

# Example: Unpacking a tuple
person = ("John", 30, "Engineer")
name, age, profession = person
print(f"Name: {name}, Age: {age}, Profession: {profession}")
# Output:
# Name: John
# Age: 30
# Profession: Engineer

# Explanation:
# - Tuple unpacking allows you to assign each value of the tuple to individual variables.


# ---------------------------
# Use case: Immutable configuration values
# ---------------------------
# Tuples are often used to store constant values, like configuration settings.

# Example: Storing immutable settings in a tuple
settings = ("dark_mode", "en_US", 1080)

# Explanation:
# - The `settings` tuple stores configuration values that should not change during program execution.
