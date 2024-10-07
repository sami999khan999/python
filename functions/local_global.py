# ---------------------------
# Modifying Global Variables Inside a Function
# ---------------------------
# To modify a global variable inside a function, you need to declare it as 'global' using the 'global' keyword.

# Example: Modifying a global variable
counter = 0  # Global variable


def increment_counter():
    """Increments the global counter variable."""
    global counter  # Declare the global variable
    counter += 1  # Modify the global variable


# Calling the function multiple times
increment_counter()
increment_counter()
print(counter)  # Output: 2

# Explanation:
# The 'increment_counter' function declares 'counter' as a global variable, allowing it to modify the global 'counter' variable.
# This demonstrates how to access and change global variables from within a function.
#
# Scope Explanation:
# - A global variable is defined outside of any function and can be accessed from anywhere in the code.
# - Inside a function, you must use the 'global' keyword to modify a global variable; otherwise, it will be treated as a local variable.

# ---------------------------
# Local and Global Variables with the Same Name
# ---------------------------
# If a local variable has the same name as a global variable, the local variable will take precedence within the function's scope.

# Example: Local variable shadows a global variable
value = 10  # Global variable


def shadow_variable():
    """Demonstrates shadowing of a global variable by a local variable."""
    value = 5  # Local variable with the same name
    print("Inside function:", value)  # Output: Inside function: 5


# Calling the function
shadow_variable()
print("Outside function:", value)  # Output: Outside function: 10

# Explanation:
# In the 'shadow_variable' function, the local variable 'value' shadows the global variable 'value'.
# Inside the function, it refers to the local variable, while outside the function, it refers to the global variable.
# This shows how variable scope works in Python, where local variables can mask global ones if they share the same name.
#
# Scope Explanation:
# - A local variable is defined within a function and can only be accessed within that function.
# - When a local variable has the same name as a global variable, the local variable takes precedence inside the function,
# meaning that any reference to that variable name will refer to the local variable rather than the global one.
