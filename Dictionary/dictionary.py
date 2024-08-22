# dictionary

# A dictionary in Python is an unordered, mutable collection of key-value pairs. Each key in a dictionary is unique and is used to access the corresponding value. Dictionaries are commonly used to store and retrieve data where a unique identifier (the key) is associated with each value.

my_dict = {"name": "John Doe", "age": 30, "city": "New York"}

print(my_dict)

# ===================================================================================================== #

# accessing values

# access the value associated with a specific key by using square brackets []. If you try to access a key that doesn't exist, Python will raise a KeyError.

print(my_dict["name"])
print(my_dict["age"])

# To avoid this, you can use the get() method, which returns None (or a default value) if the key is not found.

print(my_dict.get("city"))

# ===================================================================================================== #

# adding and Modifying Dictionary Entries

# we can add a new key-value pair or update an existing key by simply assigning a value to the key.

my_dict["address"] = "123 Main St"
print(my_dict)

my_dict["age"] = 31
print(my_dict)
