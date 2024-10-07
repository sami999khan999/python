# ---------------------------
# Functions Use Case
# ---------------------------
# Functions are reusable blocks of code that perform specific tasks.
# They help organize code, reduce redundancy, and improve readability.
# Functions can be defined to take inputs (parameters) and return outputs (results).


# Example: Function to greet a user
def greet(name):
    """Returns a greeting message for the user."""
    return f"Hello, {name}!"


# Calling the function
print(greet("Alice"))  # Output: Hello, Alice!

# Explanation:
# In this example, the function 'greet' takes one parameter, 'name', and returns a greeting message.
# This showcases the basic use of functions to encapsulate behavior and improve code clarity.

# ---------------------------
# Function with Parameters
# ---------------------------
# Functions can accept parameters, allowing you to pass data into them.
# This makes functions flexible and reusable for different inputs.


# Example: Function to add two numbers
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b


# Calling the function with arguments
result = add(5, 3)
print(result)  # Output: 8


# Example: Function to concatenate two strings
def concatenate(string1, string2):
    """Returns the concatenation of two strings."""
    return string1 + " " + string2


# Calling the function with string arguments
greeting = concatenate("Hello", "World")
print(greeting)  # Output: Hello World

# Explanation:
# This section illustrates how functions can take parameters.
# The 'add' function adds two numbers together, while the 'concatenate' function combines two strings.
# Both functions demonstrate how parameters can enhance a function's versatility.

# ---------------------------
# Default Parameters
# ---------------------------
# You can provide default values for parameters in functions.
# If no argument is passed for a parameter, the default value is used.


# Example: Function with a default parameter
def multiply(a, b=2):
    """Returns the product of a and b. Defaults b to 2 if not provided."""
    return a * b


# Calling the function with one argument (uses default for b)
print(multiply(4))  # Output: 8 (4 * 2)

# Calling the function with both arguments
print(multiply(4, 3))  # Output: 12 (4 * 3)


# Example: Function to describe a pet with a default value
def describe_pet(pet_name, pet_type="dog"):
    """Returns a description of the pet."""
    return f"{pet_name} is a {pet_type}."


# Calling the function with one argument (uses default for pet_type)
print(describe_pet("Buddy"))  # Output: Buddy is a dog.
# Calling the function with both arguments
print(describe_pet("Whiskers", "cat"))  # Output: Whiskers is a cat.

# Explanation:
# In this section, we explore default parameters.
# The 'multiply' function multiplies two numbers, using 2 as a default for the second parameter if none is provided.
# The 'describe_pet' function allows for flexibility by providing a default pet type.
# This feature simplifies function calls when the default behavior is sufficient.
