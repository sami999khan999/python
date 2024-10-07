# ---------------------------
# Basic for loop
# ---------------------------
# A `for` loop is used to iterate over items in a sequence (list, tuple, etc.).

# Example: Loop through a list of numbers
numbers = [1, 2, 3, 4, 5]

# Loop through each number in the list.
for num in numbers:
    print(num)  # Output: 1, 2, 3, 4, 5

# Use case: Summing numbers in a list
total = 0
for num in numbers:
    total += num  # Accumulate the sum of the numbers
print(f"Total: {total}")  # Output: Total: 15

# Explanation:
# - The loop iterates over each number, adding it to the `total` variable.
# - At the end of the loop, the total sum is printed.


# ---------------------------
# Loop through a string
# ---------------------------
# You can iterate through the characters in a string.

# Example: Loop through each character in a string
word = "Python"

# Loop through each character.
for char in word:
    print(char)  # Output: P, y, t, h, o, n

# Use case: Count vowels in a string
vowels = "aeiou"
vowel_count = 0
for char in word.lower():
    if char in vowels:
        vowel_count += 1
print(f"Vowel count: {vowel_count}")  # Output: Vowel count: 1

# Explanation:
# - The loop checks each character in the string.
# - If the character is a vowel, the `vowel_count` is incremented.


# ---------------------------
# Using range() function
# ---------------------------
# `range()` generates a sequence of numbers, useful in loops.

# Example: Loop from 0 to 4 (5 is not included)
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4

# Example: Custom range with start and step
for i in range(1, 10, 2):
    print(i)  # Output: 1, 3, 5, 7, 9

# Use case: Loop through indexes of a list
colors = ["red", "green", "blue"]
for i in range(len(colors)):
    print(f"Index {i}: {colors[i]}")
# Output:
# Index 0: red
# Index 1: green
# Index 2: blue

# Explanation:
# - `range(1, 10, 2)` generates numbers starting from 1, incrementing by 2.
# - Using `range(len(list))` allows you to access both index and item from a list.


# ---------------------------
# Using break to exit a loop
# ---------------------------
# The `break` statement stops the loop immediately.

# Example: Exit the loop when a condition is met
for num in numbers:
    if num == 3:
        break  # Stop loop when num is 3
    print(num)  # Output: 1, 2

# Use case: Searching for an item in a list
item_to_find = 3
for num in numbers:
    if num == item_to_find:
        print(f"Item {num} found!")  # Output: Item 3 found!
        break

# Explanation:
# - The loop stops executing as soon as `num == 3`.
# - The loop doesn't print 4 or 5 because it exits before reaching them.


# ---------------------------
# Using continue to skip an iteration
# ---------------------------
# The `continue` statement skips the current iteration and goes to the next.

# Example: Skip printing the number 3
for num in numbers:
    if num == 3:
        continue  # Skip the rest of the code in this iteration
    print(num)  # Output: 1, 2, 4, 5

# Use case: Skip even numbers in a list
for num in numbers:
    if num % 2 == 0:
        continue  # Skip even numbers
    print(f"Odd number: {num}")  # Output: Odd number: 1, 3, 5

# Explanation:
# - The loop skips over the number 3 and continues with the next iteration.
# - In the second example, only odd numbers are printed.


# ---------------------------
# Nested for loops
# ---------------------------
# A `for` loop inside another loop is called a nested loop.

# Example: Create a multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} * {j} = {i * j}")
# Output:
# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
# 2 * 1 = 2
# 2 * 2 = 4
# 2 * 3 = 6
# 3 * 1 = 3
# 3 * 2 = 6
# 3 * 3 = 9

# Use case: Generate a grid of coordinates
for x in range(3):
    for y in range(3):
        print(f"Coordinate: ({x}, {y})")
# Output:
# Coordinate: (0, 0)
# Coordinate: (0, 1)
# Coordinate: (0, 2)
# Coordinate: (1, 0)
# Coordinate: (1, 1)
# Coordinate: (1, 2)
# Coordinate: (2, 0)
# Coordinate: (2, 1)
# Coordinate: (2, 2)

# Explanation:
# - The outer loop controls the row (`i`) and the inner loop controls the column (`j`).
# - Nested loops can be useful for creating grids, tables, or iterating over multiple dimensions.


# ---------------------------
# Looping through a dictionary
# ---------------------------
# Loop through both keys and values in a dictionary.

# Example: Loop through a dictionary's keys and values
student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78}

# Loop through the dictionary using the items() method.
for name, score in student_scores.items():
    print(f"{name}: {score}")
# Output:
# Alice: 85
# Bob: 92
# Charlie: 78

# Use case: Calculate average score of students
total_score = 0
for name, score in student_scores.items():
    total_score += score
average_score = total_score / len(student_scores)
print(f"Average score: {average_score}")  # Output: Average score: 85.0

# Explanation:
# - The `for` loop iterates over both the key (student name) and value (student score).
# - You can access both the key and value in each iteration.
