# ---------------------------
# Creating and Manipulating Sets
# ---------------------------
# A set in Python is an unordered collection of unique items.
# Sets are mutable, meaning you can add or remove items.

# Example: Creating a set
fruits = {"apple", "banana", "cherry"}
print(fruits)  # Output: {'banana', 'apple', 'cherry'}

# Explanation:
# - The set `fruits` contains three unique elements.
# - Sets are created using curly braces `{}` or the `set()` constructor.

# ---------------------------
# Adding Items to a Set
# ---------------------------
# Use the `add()` method to add a single element to a set.

# Example: Adding an item to a set
fruits.add("orange")
print(fruits)  # Output: {'banana', 'apple', 'cherry', 'orange'}

# Explanation:
# - The `add()` method adds the item "orange" to the `fruits` set.


# ---------------------------
# Removing Items from a Set
# ---------------------------
# Use the `remove()` method to remove an item from a set.
# If the item is not found, it raises a KeyError.
# Alternatively, use the `discard()` method to remove an item without raising an error.

# Example: Removing an item from a set
fruits.remove("banana")
print(fruits)  # Output: {'apple', 'cherry', 'orange'}

# Example: Using discard() to remove an item
fruits.discard("grape")  # Does not raise an error even if "grape" is not in the set
print(fruits)  # Output: {'apple', 'cherry', 'orange'}

# ---------------------------
# Union of Sets
# ---------------------------
# The `union()` method returns a new set containing all unique elements from both sets.

# Example: Performing union of two sets
vegetables = {"carrot", "potato", "onion"}
combined = fruits.union(vegetables)
print(combined)  # Output: {'apple', 'cherry', 'orange', 'carrot', 'potato', 'onion'}

# Explanation:
# - The `union()` method combines the elements of the `fruits` and `vegetables` sets.


# ---------------------------
# Other Useful Set Methods
# ---------------------------

# 1. **Intersection**: Get common elements from two sets using the `intersection()` method.
# Example: Finding common elements between two sets
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
common_elements = set_a.intersection(set_b)
print(common_elements)  # Output: {3, 4}

# 2. **Difference**: Get elements that are in one set but not in another using the `difference()` method.
# Example: Finding elements in set_a that are not in set_b
unique_to_a = set_a.difference(set_b)
print(unique_to_a)  # Output: {1, 2}

# 3. **Symmetric Difference**: Get elements that are in either of the sets but not in both using `symmetric_difference()`.
# Example: Finding unique elements from both sets
unique_elements = set_a.symmetric_difference(set_b)
print(unique_elements)  # Output: {1, 2, 5, 6}

# 4. **Length of a Set**: Use the `len()` function to get the number of items in a set.
# Example: Finding the length of a set
number_of_fruits = len(fruits)
print(number_of_fruits)  # Output: 3

# 5. **Clearing a Set**: Use the `clear()` method to remove all items from a set.
# Example: Clearing all items from a set
fruits.clear()
print(fruits)  # Output: set()

# ---------------------------
# Iterating Through a Set
# ---------------------------
# You can loop through a set using a for loop to access each element.

# Example: Looping through a set
for fruit in {"apple", "banana", "cherry"}:
    print(fruit)
# Output:
# apple
# banana
# cherry

# Explanation:
# - The for loop iterates over the set, printing each fruit.

# ---------------------------
# Use case: Removing duplicates from a list
# ---------------------------
# Sets are useful for removing duplicates from a list.

# Example: Using a set to remove duplicates
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(my_list)
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}

# Explanation:
# - Converting a list to a set automatically removes duplicates.


# ---------------------------
# Use case: Checking membership
# ---------------------------
# Sets provide an efficient way to check if an item exists.

# Example: Checking membership in a set
colors = {"red", "green", "blue"}
if "red" in colors:
    print("Red is present in the set.")  # Output: Red is present in the set.
else:
    print("Red is not present in the set.")

# Explanation:
# - The `in` keyword checks if an item exists in the set.
