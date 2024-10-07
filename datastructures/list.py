# ---------------------------
# Creating and Manipulating Lists
# ---------------------------
# A list in Python is an ordered collection of items, which can store different data types.
# Lists are mutable, meaning their content can be changed after creation.

# Example: Creating a list
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Explanation:
# - The list `fruits` contains three string elements: "apple", "banana", and "cherry".
# - You can access list items by their index (starting from 0).

# Accessing list items by index:
first_fruit = fruits[0]  # Accessing the first item
last_fruit = fruits[-1]  # Accessing the last item
print(first_fruit)  # Output: apple
print(last_fruit)  # Output: cherry

# ---------------------------
# Using append() to add an item to the end of a list
# ---------------------------
# The append() method adds a new element to the end of the list.

# Example: Adding an element to the list
fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

# Explanation:
# - The new item "orange" is added to the end of the `fruits` list.


# ---------------------------
# Using insert() to add an item at a specific index
# ---------------------------
# The insert() method allows you to insert an element at a specific index.

# Example: Inserting an item at index 1
fruits.insert(1, "kiwi")
print(fruits)  # Output: ['apple', 'kiwi', 'banana', 'cherry', 'orange']

# Explanation:
# - The item "kiwi" is inserted at index 1, shifting the other elements to the right.


# ---------------------------
# Using remove() to remove an item by value
# ---------------------------
# The remove() method removes the first occurrence of a specific value from the list.

# Example: Removing an item from the list
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'kiwi', 'cherry', 'orange']

# Explanation:
# - The item "banana" is removed from the list. If the value doesn't exist, Python raises an error.


# ---------------------------
# Using sort() to sort the list in ascending order
# ---------------------------
# The sort() method sorts the list in place (modifying the original list).

# Example: Sorting the list
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
print(numbers)  # Output: [1, 1, 2, 3, 4, 5, 9]

# Explanation:
# - The `numbers` list is sorted in ascending order.
# - Sorting modifies the original list. If you need to preserve the original, use `sorted()` instead.


# ---------------------------
# Using reverse() to reverse the order of a list
# ---------------------------
# The reverse() method reverses the order of the list.

# Example: Reversing the list
numbers.reverse()
print(numbers)  # Output: [9, 5, 4, 3, 2, 1, 1]

# Explanation:
# - The `numbers` list is reversed. Like `sort()`, this method modifies the original list.


# ---------------------------
# List slicing
# ---------------------------
# List slicing allows you to access a portion (or slice) of the list using a colon (`:`) between indices.

# Example: List slicing
# Syntax: list[start:end:step] (start is inclusive, end is exclusive)
sublist = fruits[1:3]  # Get items from index 1 to 2 (3 is not included)
print(sublist)  # Output: ['kiwi', 'cherry']

# Example: Using a step in slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = numbers[::2]  # Get every second item (step=2)
print(even_numbers)  # Output: [0, 2, 4, 6, 8]

# Explanation:
# - Slicing allows you to extract specific parts of the list by specifying a start and end index.
# - The step argument allows you to skip elements (e.g., `::2` returns every second element).


# ---------------------------
# Iterating through a list using a for loop
# ---------------------------
# You can loop through a list using a for loop to access each element.

# Example: Looping through a list
for fruit in fruits:
    print(fruit)
# Output:
# apple
# kiwi
# cherry
# orange

# Explanation:
# - The `for` loop iterates over the list `fruits`, and each element is printed one by one.


# ---------------------------
# Iterating with index using enumerate()
# ---------------------------
# The enumerate() function allows you to get both the index and the value while iterating.

# Example: Looping through a list with index
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
# Output:
# Index 0: apple
# Index 1: kiwi
# Index 2: cherry
# Index 3: orange

# Explanation:
# - `enumerate()` returns both the index and value for each item in the list, which can be useful in many cases.


# ---------------------------
# Use case: Creating and modifying a to-do list
# ---------------------------
# Example: Simulating a to-do list by using append(), remove(), and other list methods
to_do_list = []

# Add tasks to the to-do list
to_do_list.append("Buy groceries")
to_do_list.append("Finish project")
to_do_list.append("Exercise")

# Remove a task once it's done
to_do_list.remove("Exercise")

# Print the updated to-do list
print(to_do_list)  # Output: ['Buy groceries', 'Finish project']

# Explanation:
# - You can create dynamic lists like a to-do list and modify them using various methods.


# ---------------------------
# Use case: Sorting a list of student grades
# ---------------------------
# Example: Sorting and reversing a list of student grades
grades = [88, 92, 79, 95, 84, 67, 73]

# Sort the grades in ascending order
grades.sort()
print(grades)  # Output: [67, 73, 79, 84, 88, 92, 95]

# Reverse the order to get the grades in descending order
grades.reverse()
print(grades)  # Output: [95, 92, 88, 84, 79, 73, 67]

# Explanation:
# - Sorting is useful for organizing data, such as student grades, in a desired order.


# ---------------------------
# Use case: List slicing to get parts of a large dataset
# ---------------------------
# Example: Simulating access to a slice of a dataset
data = ["item1", "item2", "item3", "item4", "item5", "item6", "item7"]

# Get the first 3 items
first_three = data[:3]
print(first_three)  # Output: ['item1', 'item2', 'item3']

# Get the last 3 items
last_three = data[-3:]
print(last_three)  # Output: ['item5', 'item6', 'item7']

# Explanation:
# - Slicing can be particularly useful when working with large datasets, allowing you to access specific sections without loading the entire list.
