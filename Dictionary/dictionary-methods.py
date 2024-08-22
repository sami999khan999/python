# dictionary methods

my_dictionary = {"name": "John", "age": 30, "city": "New York"}

# ===================================================================================================== #

# key

# Returns a view object of the dictionary's keys.

keys = my_dictionary.keys()
print(keys)

# ===================================================================================================== #

# values

# Returns a view object of the dictionary's key-value pairs as tuples.

values = my_dictionary.values()
print(values)

# ===================================================================================================== #

# items

# Returns a view object of the dictionary's key-value pairs as tuples.

items = my_dictionary.items()
print(items)

# ===================================================================================================== #

# update

# Updates the dictionary with the key-value pairs from another dictionary or iterable of key-value pairs.

my_dictionary.update({"age": 300, "name": "sami"})

print(my_dictionary)

# ===================================================================================================== #

# pop

# Removes the specified key and returns the corresponding value. Raises a KeyError if the key is not found.

removed_value = my_dictionary.pop("city")
print(removed_value)
print(my_dictionary)

# ===================================================================================================== #

# popitem

# Removes and returns the last inserted key-value pair as a tuple. (In Python 3.7+, the order is maintained; before Python 3.7, the order is arbitrary.)

last_ltem = my_dictionary.popitem()

print(last_ltem)
print(my_dictionary)

# ===================================================================================================== #

# del

# Deletes the specified key or the entire dictionary.

del my_dictionary["name"]

print(my_dictionary)

# ===================================================================================================== #
