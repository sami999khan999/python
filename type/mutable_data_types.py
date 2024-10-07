# ---------------------------
# What is Mutable?
# ---------------------------
# Mutability means that an object’s state can be changed after it is created.
# Mutable objects in Python include lists, dictionaries, and sets.
# You can modify, add, or remove elements in mutable objects without creating a new object.

# ---------------------------
# Mutable Lists
# ---------------------------
# Lists are mutable in Python, meaning you can modify their contents.
# You can change individual elements, append new elements, or remove elements.

list_example = [1, 2, 3]  # Example list

# Modify an element
list_example[0] = 10  # Changing the first element to 10

# Append an element
list_example.append(4)  # Adding 4 to the end of the list

# Remove an element
list_example.remove(2)  # Removing the value 2 from the list

print(f"The modified list is: {list_example}")  # Output: [10, 3, 4]

# ---------------------------
# Mutable Dictionaries
# ---------------------------
# Dictionaries are mutable, meaning you can change the values, add new key-value pairs, or remove existing pairs.

dict_example = {"name": "Alice", "age": 30}  # Example dictionary

# Modify a value
dict_example["age"] = 31  # Changing the value associated with "age" to 31

# Add a new key-value pair
dict_example["city"] = "New York"  # Adding a new key-value pair

# Remove a key-value pair
del dict_example["name"]  # Removing the key "name" and its value

print(
    f"The modified dictionary is: {dict_example}"
)  # Output: {'age': 31, 'city': 'New York'}

# ---------------------------
# Mutable Sets
# ---------------------------
# Sets are mutable, meaning you can add or remove elements.
# Note that sets do not allow duplicate elements and are unordered.

set_example = {1, 2, 3}  # Example set

# Add an element
set_example.add(4)  # Adding 4 to the set

# Remove an element
set_example.remove(2)  # Removing the value 2 from the set

print(f"The modified set is: {set_example}")  # Output: {1, 3, 4}
