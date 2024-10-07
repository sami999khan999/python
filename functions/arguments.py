# ---------------------------
# Variable-Length Arguments (args)
# ---------------------------
# In Python, you can define functions that accept a variable number of arguments.
# This is done using the *args syntax, allowing you to pass any number of positional arguments.


# Example: Function to calculate the sum of multiple numbers
def calculate_sum(*args):
    """Returns the sum of all the provided arguments."""
    return sum(args)


# Calling the function with different numbers of arguments
print(calculate_sum(1, 2, 3))  # Output: 6
print(calculate_sum(5, 10, 15, 20))  # Output: 50


# Example: Function to print a list of names
def print_names(*args):
    """Prints each name provided as an argument."""
    for name in args:
        print(name)


# Calling the function with a variable number of names
print_names("Alice", "Bob", "Charlie")  # Output: Alice \n Bob \n Charlie

# Explanation:
# The *args syntax allows a function to accept an arbitrary number of positional arguments.
# The 'calculate_sum' function demonstrates this by summing all provided numbers,
# while the 'print_names' function showcases how to iterate over the variable-length arguments.

# ---------------------------
# Keyword Arguments
# ---------------------------
# Keyword arguments allow you to pass arguments to a function by explicitly specifying
# the parameter names, making the code more readable and avoiding confusion.


# Example: Function with keyword arguments
def describe_person(name, age, city="Unknown"):
    """Returns a description of a person using keyword arguments."""
    return f"{name} is {age} years old and lives in {city}."


# Calling the function with keyword arguments
print(
    describe_person(name="Alice", age=30)
)  # Output: Alice is 30 years old and lives in Unknown.
print(
    describe_person(name="Bob", age=25, city="New York")
)  # Output: Bob is 25 years old and lives in New York.


# Example: Function to create a user profile with keyword arguments
def create_profile(username, email, **additional_info):
    """Creates a user profile with optional additional information."""
    profile = {
        "Username": username,
        "Email": email,
        **additional_info,  # Merging additional info into the profile
    }
    return profile


# Calling the function with keyword arguments
user_profile = create_profile(
    "alice123", "alice@example.com", age=30, location="Wonderland"
)
print(user_profile)
# Output: {'Username': 'alice123', 'Email': 'alice@example.com', 'age': 30, 'location': 'Wonderland'}

# Explanation:
# Keyword arguments provide a way to pass parameters by name, enhancing code clarity.
# The 'describe_person' function exemplifies this by clearly stating the parameters being passed.
# The 'create_profile' function demonstrates how to collect additional keyword arguments using **kwargs,
# allowing for flexibility when creating user profiles.
