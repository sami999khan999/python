# ---------------------------
# Single Quotes String
# ---------------------------
# You can define a string in Python using single quotes (' ').
# This is useful for short strings or when the string itself does not contain any single quotes.

single_quote_string = "Hello, World!"  # String using single quotes
print(single_quote_string)  # Output: Hello, World!

# If your string contains a single quote, you can use escape characters like this:
escaped_single_quote = (
    "It's a great day!"  # The single quote inside the string is escaped using \'
)
print(escaped_single_quote)  # Output: It's a great day!


# ---------------------------
# Double Quotes String
# ---------------------------
# You can also define a string using double quotes (" ").
# Double quotes are often used when the string contains single quotes, which helps avoid escape characters.

double_quote_string = "Hello, World!"  # String using double quotes
print(double_quote_string)  # Output: Hello, World!

# If your string contains single quotes, double quotes avoid the need for escape characters:
no_escape_needed = "It's a great day!"  # No need to escape the single quote
print(no_escape_needed)  # Output: It's a great day!


# ---------------------------
# Triple Single Quotes String
# ---------------------------
# Triple single quotes (''' ''') allow for multi-line strings.
# They are typically used for multi-line text or comments.

triple_single_quote_string = """This is a string
that spans multiple
lines."""
print(triple_single_quote_string)
# Output:
# This is a string
# that spans multiple
# lines.


# Triple single quotes are also useful for writing docstrings (multi-line comments in functions):
def example_function():
    """This function does something.
    It has a multi-line docstring to explain its behavior."""
    pass


# ---------------------------
# Triple Double Quotes String
# ---------------------------
# Triple double quotes (""" """) work the same way as triple single quotes.
# They also allow for multi-line strings and are commonly used for docstrings.

triple_double_quote_string = """This is another
multi-line string using
triple double quotes."""
print(triple_double_quote_string)
# Output:
# This is another
# multi-line string using
# triple double quotes.


# Triple double quotes are the standard for writing function docstrings:
def another_example_function():
    """This is a multi-line docstring using triple double quotes.
    It describes the purpose and functionality of the function."""
    pass
