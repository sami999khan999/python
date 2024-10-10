# ---------------------------
# Error List
# ---------------------------
# Python provides several built-in exceptions that can be caught and handled.
# Common exceptions include:

# - ValueError: Raised when a function receives an argument of the correct type but an inappropriate value.
# - TypeError: Raised when an operation or function is applied to an object of inappropriate type.
# - IndexError: Raised when trying to access an index that is out of range for a list or tuple.
# - KeyError: Raised when trying to access a key in a dictionary that does not exist.
# - ZeroDivisionError: Raised when attempting to divide by zero.

# Use Case:
# Understanding common exceptions helps in writing robust code that can handle potential errors gracefully.

# ---------------------------
# Simple Try-Except
# ---------------------------
# A simple try-except block allows you to catch exceptions that may arise during execution.

# Example: Simple try-except
try:
    result = 10 / 0  # Attempting to divide by zero
except ZeroDivisionError as e:
    print("Error:", e)  # Output: Error: division by zero

# Explanation:
# The 'try' block contains code that may raise an exception.
# The 'except' block catches the specific exception (in this case, ZeroDivisionError) and executes the code within it.

# Use Case:
# Using try-except to catch and handle errors during calculations, ensuring the program doesn't crash.

# ---------------------------
# Handling Multiple Exceptions
# ---------------------------
# You can handle multiple exceptions using a single except block or separate blocks.

# Example: Handling multiple exceptions
try:
    number = int(input("Enter a number: "))  # Attempting to convert input to an integer
    result = 10 / number  # Division operation
except ValueError as ve:
    print("Invalid input! Please enter a valid number.", ve)  # Handling ValueError
except ZeroDivisionError as zde:
    print("Error: Cannot divide by zero.", zde)  # Handling ZeroDivisionError

# Explanation:
# The code checks for multiple exceptions that might arise: ValueError for invalid input and ZeroDivisionError for division by zero.
# Each exception has its own handling code.

# Use Case:
# Useful when working with user inputs where various errors can occur.

# ---------------------------
# Catching All Exceptions
# ---------------------------
# To catch any exception, you can use a general except clause without specifying an exception type.

# Example: Catching all exceptions
try:
    result = 10 / int(input("Enter a number: "))  # Attempt to divide by user input
except Exception as e:
    print(
        "An error occurred:", e
    )  # Output: An error occurred: division by zero or invalid input

# Explanation:
# The 'except Exception' block catches any exception, providing a generic way to handle errors.
# However, this is less specific and may make debugging harder.

# Use Case:
# Catching all exceptions is useful for logging errors or when you want to ensure that the program continues running.

# ---------------------------
# Finally Block
# ---------------------------
# The 'finally' block is used to execute code that should run regardless of whether an exception was raised or not.

# Example: Using finally block
try:
    file = open("example.txt", "r")  # Attempting to open a file
    content = file.read()
except FileNotFoundError as e:
    print("Error: File not found.", e)
finally:
    if "file" in locals():
        file.close()  # Ensure the file is closed if it was opened

# Explanation:
# The 'finally' block executes after the try-except blocks, ensuring that resources (like files) are properly released.
# It’s useful for cleanup actions.

# Use Case:
# Ensuring that files or network connections are closed after their usage, preventing resource leaks.
