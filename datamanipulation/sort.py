# ---------------------------
# Sorting Lists in Ascending Order
# ---------------------------
# Python provides built-in methods to sort lists.
# Sorting can be done in ascending order, which arranges elements from smallest to largest.


# Example: Sorting a list in ascending order
names = ["Charlie", "Bob", "Ethan", "Alice", "Fiona", "George", "Hannah", "Diana"]
names.sort()  # Sorts the list in-place
print(
    names
)  # Output: ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan', 'Fiona', 'George', 'Hannah']

# Explanation:
# The 'sort()' method sorts the elements of the list in ascending order by default.
# This is useful for organizing data alphabetically or numerically, making it easier to read and analyze.


# ---------------------------
# Sorting Lists in Descending Order
# ---------------------------
# You can sort lists in descending order by using the reverse parameter.
# This arranges elements from largest to smallest.


# Example: Sorting a list in descending order
students = ["Charlie", "Bob", "Ethan", "Alice", "Fiona", "George", "Hannah", "Diana"]
students.sort(reverse=True)  # Sorts the list in reverse order
print(
    students
)  # Output: ['Hannah', 'George', 'Fiona', 'Ethan', 'Diana', 'Charlie', 'Bob', 'Alice']

# Explanation:
# By setting the 'reverse' parameter to True, the 'sort()' method arranges the elements in descending order.
# This is useful when you want to highlight the highest values or most significant entries.


# ---------------------------
# Sorting Tuples
# ---------------------------
# You can use the sorted() function to sort tuples, which returns a new sorted list.
# Tuples are immutable, meaning they cannot be changed after creation, so sorted() is preferred.


# Example: Using sorted() to sort a tuple
students_tuple = (
    "Charlie",
    "Bob",
    "Ethan",
    "Alice",
    "Fiona",
    "George",
    "Hannah",
    "Diana",
)

sorted_students = sorted(students_tuple)  # sorted() returns a new sorted list
print(
    sorted_students
)  # Output: ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan', 'Fiona', 'George', 'Hannah']

# Explanation:
# The 'sorted()' function creates a new list that contains the elements of the tuple in sorted order.
# This is useful for working with tuples where you need a sorted version without altering the original tuple.


# ---------------------------
# Sorting a List of Tuples
# ---------------------------
# You can sort lists that contain tuples based on the elements of the tuples.
# By default, sorting is done based on the first element of each tuple.


# Example: Sorting a list of tuples
students_data = [
    ("Charlie", 19, "C"),
    ("Diana", 21, "A"),
    ("Alice", 20, "A"),
    ("Bob", 22, "B"),
]

# Sorting by the first element (name) in ascending order
students_data.sort()
print(students_data)
# Output: [('Alice', 20, 'A'), ('Bob', 22, 'B'), ('Charlie', 19, 'C'), ('Diana', 21, 'A')]

# Explanation:
# The 'sort()' method sorts the list of tuples based on the first element of each tuple (in this case, the name).
# This allows for easy organization of data containing multiple attributes.


# ---------------------------
# Sorting a List of Tuples in Descending Order
# ---------------------------
# You can also sort lists of tuples in descending order based on specific elements.
# This is useful for prioritizing certain values.


# Example: Sorting a list of tuples in descending order by age
students_data.sort(
    key=lambda grades: grades[1], reverse=True
)  # Sort by age in descending order
print(students_data)
# Output: [('Bob', 22, 'B'), ('Diana', 21, 'A'), ('Alice', 20, 'A'), ('Charlie', 19, 'C')]

# Explanation:
# The 'sort()' method with a key function (in this case, a lambda function that extracts the second element)
# allows sorting based on specific criteria. By setting 'reverse=True', the tuples are sorted in descending order by age,
# which is useful for displaying the highest values first.


# ---------------------------
# Custom Sorting with a Key Function
# ---------------------------
# You can customize the sorting behavior using a key function.
# This allows sorting based on specific criteria rather than just the first element.


# Example: Custom sorting with a key function
grad = lambda grades: grades[1]  # Extract the second element (age) for sorting

# Sorting by age in descending order
students_data.sort(key=grad, reverse=True)
print(students_data)
# Output: [('Bob', 22, 'B'), ('Diana', 21, 'A'), ('Alice', 20, 'A'), ('Charlie', 19, 'C')]

# Explanation:
# By providing a key function (in this case, a lambda function that extracts the second element of each tuple), you can sort the list based on that specific value.
# Setting 'reverse=True' arranges the results in descending order, which is helpful for prioritizing higher values.
