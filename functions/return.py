# ---------------------------
# Return Statements
# ---------------------------
# A return statement is used in a function to send a result back to the caller.
# When a return statement is executed, the function ends, and control goes back to the caller.


# Example: Function to square a number
def square(num):
    """Returns the square of the given number."""
    return num**2


# Calling the function
result = square(4)
print(result)  # Output: 16

# Explanation:
# The 'square' function returns the square of the input number using a return statement.
# This demonstrates the basic use of return to output a value from a function.

# ---------------------------
# Returning a Single Value
# ---------------------------
# Functions can return a single value using the return statement.


# Example: Function to find the maximum of two numbers
def max_number(a, b):
    """Returns the maximum of two numbers."""
    return a if a > b else b


# Calling the function
print(max_number(10, 20))  # Output: 20

# Explanation:
# The 'max_number' function compares two numbers and returns the maximum.
# This illustrates how a function can return a single, specific result.

# ---------------------------
# Returning Multiple Values
# ---------------------------
# Functions can return multiple values as a tuple.


# Example: Function to calculate both the sum and product of two numbers
def calculate(a, b):
    """Returns the sum and product of two numbers."""
    return a + b, a * b


# Calling the function
sum_value, product_value = calculate(4, 5)
print(f"Sum: {sum_value}, Product: {product_value}")  # Output: Sum: 9, Product: 20

# Explanation:
# The 'calculate' function returns two values, which are automatically packed into a tuple.
# This shows how multiple results can be returned and unpacked by the caller.

# ---------------------------
# Returning Nothing
# ---------------------------
# A function can also return nothing, which is equivalent to returning None.


# Example: Function to print a message
def greet_user(name):
    """Prints a greeting message and returns nothing."""
    print(f"Hello, {name}!")


# Calling the function
result = greet_user("Alice")  # Output: Hello, Alice!
print(result)  # Output: None

# Explanation:
# The 'greet_user' function prints a greeting message but does not return a value.
# When a function reaches the end without a return statement, it returns None by default.

# ---------------------------
# Returning a List
# ---------------------------
# Functions can return a list containing multiple elements.


# Example: Function to generate a list of squares
def generate_squares(n):
    """Returns a list of squares from 0 to n-1."""
    return [i**2 for i in range(n)]


# Calling the function
squares = generate_squares(5)
print(squares)  # Output: [0, 1, 4, 9, 16]

# Explanation:
# The 'generate_squares' function returns a list of squares of numbers up to n-1.
# This demonstrates how functions can produce complex data types like lists.

# ---------------------------
# Returning a Dictionary
# ---------------------------
# Functions can return a dictionary for key-value pairs.


# Example: Function to create a user profile
def create_profile(name, age):
    """Returns a dictionary representing a user profile."""
    return {"Name": name, "Age": age}


# Calling the function
profile = create_profile("Alice", 30)
print(profile)  # Output: {'Name': 'Alice', 'Age': 30}

# Explanation:
# The 'create_profile' function constructs and returns a dictionary containing user details.
# This highlights how functions can encapsulate structured data in a dictionary format.

# ---------------------------
# Using Return for Early Exit
# ---------------------------
# A return statement can be used to exit a function early based on a condition.


# Example: Function to check if a number is positive
def check_positive(num):
    """Returns True if the number is positive, else exits early."""
    if num <= 0:
        return False  # Early exit for non-positive numbers
    return True


# Calling the function
print(check_positive(5))  # Output: True
print(check_positive(-3))  # Output: False

# Explanation:
# The 'check_positive' function uses a return statement to exit early if the input is non-positive.
# This demonstrates how return statements can control the flow of execution within a function.
