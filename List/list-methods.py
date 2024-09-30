# Python List Methods Example

# Initial list for demonstration
numbers = [1, 2, 3, 4, 5]

# =========================================================================================== #

# 1. append()
# Adds an item to the end of the list.
numbers.append(6)
print("After append(6):", numbers)  # Output: [1, 2, 3, 4, 5, 6]

# =========================================================================================== #

# 2. extend()
# Extends the list by appending elements from an iterable (e.g., another list).
more_numbers = [7, 8]
numbers.extend(more_numbers)
print("After extend([7, 8]):", numbers)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# =========================================================================================== #

# 3. insert()
# Inserts an item at a specified position in the list.
numbers.insert(0, 9)
print("After insert(0, 9):", numbers)  # Output: [9, 1, 2, 3, 4, 5, 6, 7, 8]

# =========================================================================================== #

# 4. remove()
# Removes the first occurrence of the specified item from the list.
numbers.remove(5)
print("After remove(5):", numbers)  # Output: [9, 1, 2, 3, 4, 6, 7, 8]

# =========================================================================================== #

# 5. pop()
# Removes and returns the item at the specified index. If no index is specified, it removes the last item.
popped_item = numbers.pop()
print("After pop():", popped_item)  # Output: 8
print("List after pop():", numbers)  # Output: [9, 1, 2, 3, 4, 6, 7]

# You can also specify an index to pop an item.
popped_first_item = numbers.pop(0)
print("After pop(0):", popped_first_item)  # Output: 9
print("List after pop(0):", numbers)  # Output: [1, 2, 3, 4, 6, 7]

# =========================================================================================== #

# 6. index()
# Returns the index of the first occurrence of the specified item.
index_of_4 = numbers.index(4)
print("Index of 4:", index_of_4)  # Output: 3

# =========================================================================================== #

# 7. sort()
# Sorts the list in ascending order by default. Use reverse=True to sort in descending order.
numbers.sort()
print("After sort():", numbers)  # Output: [1, 2, 3, 4, 6, 7]

numbers.sort(reverse=True)
print("After sort(reverse=True):", numbers)  # Output: [7, 6, 4, 3, 2, 1]

# =========================================================================================== #

# 8. reverse()
# Reverses the items of the list in place.
numbers.reverse()
print("After reverse():", numbers)  # Output: [1, 2, 3, 4, 6, 7]

# =========================================================================================== #

# 9. copy()
# Returns a shallow copy of the list.
copy_of_numbers = numbers.copy()
print("Copy of numbers:", copy_of_numbers)  # Output: [1, 2, 3, 4, 6, 7]

# =========================================================================================== #

# 10. clear()
# Removes all items from the list.
numbers.clear()
print("After clear():", numbers)  # Output: []
