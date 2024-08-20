# list

# A list is a versatile and mutable (modifiable) collection data type in Python that can hold an ordered sequence of items. Lists can store elements of different data types (e.g., integers, strings, other lists) and are one of the most commonly used data structures in Python.

food = ["pizza", "burger", "pasta", "hotdog"]

print(food)
print(food[0])

food[0] = "apple"
print(food[0])
print(type(food))

# ===================================================================================================== #

mexed_list = [1, "apple", 3.1416, True]

for i in mexed_list:
    print(i, type(i))
