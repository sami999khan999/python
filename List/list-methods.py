# list methods

numbers = [1, 2, 3, 4, 5]

# ===================================================================================================== #

# append

# Adds an item to the end of the list.

numbers.append(6)
print(numbers)

# ===================================================================================================== #

# extend

# Extends the list by appending elements from an iterable (like another list).

more_numbers = [7, 8]

numbers.extend(more_numbers)
print(numbers)

# ===================================================================================================== #

# insert

# Inserts an item at a specified position in the list.

numbers.insert(0, 9)
print(numbers)

# ===================================================================================================== #

# remove

# Removes the first occurrence of the specified item from the list.

numbers.remove(5)
print(numbers)

# ===================================================================================================== #

# pop

# Removes and returns the item at the specified index. If no index is specified, it removes and returns the last item.

fruit = numbers.pop()
print(fruit)

with_index = numbers.pop(0)
print(with_index)

# ===================================================================================================== #

# index

# Returns the index of the first occurrence of the specified item.

fruit_index = numbers.index(4)
print(fruit_index)

# ===================================================================================================== #

# sort

# Sorts the list in ascending order by default. The key parameter allows you to specify a function to be called on each list element prior to making comparisons. The reverse parameter, if set to True, sorts the list in descending order.

numbers.sort()  # alphabetically sort
print(numbers)

numbers.sort(reverse=True)
print(numbers)

# ===================================================================================================== #

# reverse

numbers.reverse()
print(numbers)

# ===================================================================================================== #

# copy

# Returns a shallow copy of the list.

copy_numbers = numbers.copy()
print(copy_numbers)

# ===================================================================================================== #

# clear

# Removes all items from the list.

numbers.clear()
print(numbers)
