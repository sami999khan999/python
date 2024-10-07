# ---------------------------
# Explicit Type Conversion
# ---------------------------
# Explicit type conversion (also called type casting) is when you manually convert
# one data type to another using Python's built-in functions like int(), float(), str(), etc.

# Converting an integer to a float
int_value = 10
float_value = float(int_value)  # Convert int to float
print(f"Explicit Conversion to Float: {float_value}")  # Output: 10.0

# Converting a float to an integer (truncates the decimal part)
float_value = 3.99
int_value = int(float_value)  # Convert float to int
print(f"Explicit Conversion to Integer: {int_value}")  # Output: 3

# Converting a string to an integer
string_value = "42"
int_value = int(string_value)  # Convert string to int
print(f"Explicit Conversion to Integer: {int_value}")  # Output: 42

# Converting a list to a set (removes duplicates)
list_example = [1, 2, 2, 3]
set_example = set(list_example)  # Convert list to set
print(f"Explicit Conversion to Set: {set_example}")  # Output: {1, 2, 3}


# ---------------------------
# Implicit Type Conversion
# ---------------------------
# Implicit type conversion is when Python automatically converts one data type to another.
# This usually happens when you mix different types in an expression.
# Python will promote types to avoid data loss (e.g., converting int to float).

int_value = 10
float_value = 2.5

# Here, Python automatically converts int_value to float to perform the addition
result = int_value + float_value  # int_value is implicitly converted to float
print(f"Implicit Conversion Result: {result}")  # Output: 12.5

# In this case, int_value is promoted to a float to avoid loss of precision


# ---------------------------
# Handling Conversion Errors
# ---------------------------
# When trying to convert a value that cannot be cast (e.g., converting "Hello" to int),
# Python will raise a ValueError.
# We can handle these errors using try-except blocks.

string_value = "42"  # This will work fine
try:
    int_value = int(string_value)  # Convert string to int
    print(f"Converted value: {int_value}")  # Output: 42
except ValueError:
    print("Error: Cannot convert string to integer")

string_value = "Hello"  # This will cause an error
try:
    int_value = int(string_value)  # This will raise a ValueError
except ValueError:
    print(f"Error: '{string_value}' cannot be converted to an integer")

# Output: Error: 'Hello' cannot be converted to an integer

# You can use similar error handling for other conversions like float(), list(), set(), etc.
