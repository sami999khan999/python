# ---------------------------
# What is Immutable?
# ---------------------------
# Immutability means that once an object is created, its state cannot be changed.
# Immutable objects in Python include numbers, strings, tuples, and frozensets.
# Trying to modify the contents of an immutable object will raise an error.

# ---------------------------
# Immutable Floating-point
# ---------------------------
# Floating-point numbers are immutable in Python.
# Once a float is created, its value cannot be changed.

float_value = 3.14  # Example floating-point number

# If we try to change the value, we are actually creating a new object, not modifying the original one.
float_value = 2.71  # Reassigning creates a new float object

print(f"The value of float_value is: {float_value}")  # Output: 2.71

# ---------------------------
# Immutable Frozen Sets
# ---------------------------
# A frozen set is an immutable version of a set.
# Once a frozenset is created, you cannot add or remove elements.

frozen_set_example = frozenset([1, 2, 3])  # Example frozen set

# Trying to modify a frozenset will raise an AttributeError.
# frozen_set_example.add(4)  # This would raise an error because frozensets are immutable

print(f"The frozen set is: {frozen_set_example}")  # Output: frozenset({1, 2, 3})

# ---------------------------
# Immutable Integers
# ---------------------------
# Integers are immutable in Python.
# Once an integer object is created, its value cannot be changed.

int_value = 42  # Example integer

# Reassigning the variable creates a new integer object.
int_value = 100  # New integer object is created, original is unchanged

print(f"The value of int_value is: {int_value}")  # Output: 100

# ---------------------------
# Immutable Strings
# ---------------------------
# Strings are immutable in Python.
# Once a string is created, we cannot modify its characters directly.

string_value = "Hello, World!"  # Example string

# Modifying a string would involve creating a new string, not altering the existing one.
new_string_value = string_value.replace("World", "Python")  # This creates a new string

print(f"The original string is: {string_value}")  # Output: Hello, World!
print(f"The new string is: {new_string_value}")  # Output: Hello, Python!

# ---------------------------
# Immutable Tuples
# ---------------------------
# Tuples are immutable in Python.
# Once a tuple is created, its elements cannot be changed, added, or removed.

tuple_example = (1, 2, 3)  # Example tuple

# Trying to modify a tuple will raise an error.
# tuple_example[0] = 10  # This would raise a TypeError because tuples are immutable

print(f"The tuple is: {tuple_example}")  # Output: (1, 2, 3)
