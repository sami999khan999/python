# ---------------------------
# Creating and Manipulating Dictionaries
# ---------------------------
# A dictionary in Python is an unordered collection of key-value pairs.
# Each key must be unique, and values can be of any data type.

# Example: Creating a dictionary
student = {"name": "Alice", "age": 21, "major": "Computer Science"}
print(student)  # Output: {'name': 'Alice', 'age': 21, 'major': 'Computer Science'}

# Explanation:
# - The dictionary `student` contains keys "name", "age", and "major" with their respective values.

# ---------------------------
# Accessing Dictionary Elements
# ---------------------------
# Use the keys to access values in a dictionary.

# Example: Accessing a value by key
print(student["name"])  # Output: Alice

# Explanation:
# - The value associated with the key "name" is accessed using square brackets.

# ---------------------------
# Dictionary Methods
# ---------------------------

# 1. **keys()**: Returns a view object that displays a list of all the keys in the dictionary.
# Example: Getting keys from a dictionary
keys = student.keys()
print(keys)  # Output: dict_keys(['name', 'age', 'major'])

# 2. **values()**: Returns a view object that displays a list of all the values in the dictionary.
# Example: Getting values from a dictionary
values = student.values()
print(values)  # Output: dict_values(['Alice', 21, 'Computer Science'])

# 3. **items()**: Returns a view object that displays a list of a dictionary's key-value tuple pairs.
# Example: Getting key-value pairs from a dictionary
items = student.items()
print(
    items
)  # Output: dict_items([('name', 'Alice'), ('age', 21), ('major', 'Computer Science')])

# ---------------------------
# Updating Dictionary
# ---------------------------
# The `update()` method updates a dictionary with elements from another dictionary or from an iterable of key-value pairs.

# Example: Updating a dictionary
student.update({"age": 22, "graduation_year": 2024})
print(
    student
)  # Output: {'name': 'Alice', 'age': 22, 'major': 'Computer Science', 'graduation_year': 2024}

# Explanation:
# - The `update()` method changes the value of the key "age" and adds a new key-value pair.

# ---------------------------
# Removing Items from a Dictionary
# ---------------------------
# Use the `pop()` method to remove a specified key and return its value.
# Use `clear()` to remove all items from the dictionary.

# Example: Removing an item using pop()
removed_value = student.pop("major")
print(removed_value)  # Output: Computer Science
print(student)  # Output: {'name': 'Alice', 'age': 22, 'graduation_year': 2024}

# Explanation:
# - The `pop()` method removes the key "major" from the dictionary and returns its value.

# Example: Clearing all items from a dictionary
student.clear()
print(student)  # Output: {}

# Explanation:
# - The `clear()` method removes all key-value pairs from the dictionary.

# ---------------------------
# Use case: Storing contact information
# ---------------------------
# Dictionaries are often used to store related data together.

# Example: Creating a contact dictionary
contact = {"name": "Bob", "phone": "123-456-7890", "email": "bob@example.com"}
print(contact)

# Accessing contact details
print(contact["phone"])  # Output: 123-456-7890

# Updating the email
contact.update({"email": "bob_new@example.com"})
print(contact)  # Updated contact dictionary

# Removing the phone number
contact.pop("phone")
print(contact)  # Output: {'name': 'Bob', 'email': 'bob_new@example.com'}

# ---------------------------
# Iterating Through a Dictionary
# ---------------------------
# You can loop through a dictionary using a for loop to access keys, values, or key-value pairs.

# Example: Looping through a dictionary
for key, value in student.items():
    print(f"{key}: {value}")

# Explanation:
# - The for loop iterates over the `items()` of the dictionary, printing each key and its corresponding value.

# ---------------------------
# Use case: Counting occurrences
# ---------------------------
# Dictionaries can be used to count occurrences of elements in a list.

# Example: Counting occurrences of elements in a list
fruits = ["apple", "banana", "apple", "orange", "banana", "banana"]
fruit_count = {}

for fruit in fruits:
    if fruit in fruit_count:
        fruit_count[fruit] += 1  # Increment count
    else:
        fruit_count[fruit] = 1  # Initialize count

print(fruit_count)  # Output: {'apple': 2, 'banana': 3, 'orange': 1}
