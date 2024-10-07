# ---------------------------
# Convert to Uppercase
# ---------------------------
# Converting all characters to uppercase.
text = "good morning"
upper_text = text.upper()  # Converts all lowercase letters to uppercase.
print(upper_text)  # Output: GOOD MORNING

# Another example:
message = "welcome to python programming!"
print(message.upper())  # Output: WELCOME TO PYTHON PROGRAMMING!


# ---------------------------
# Convert to Lowercase
# ---------------------------
# Converting all characters to lowercase.
text = "GOOD NIGHT"
lower_text = text.lower()  # Converts all uppercase letters to lowercase.
print(lower_text)  # Output: good night

# Another example:
shout = "PYTHON IS FUN!"
print(shout.lower())  # Output: python is fun!


# ---------------------------
# Capitalize the First Letter
# ---------------------------
# Converting the first character to uppercase and others to lowercase.
text = "python programming"
capitalized_text = text.capitalize()  # Capitalizes the first character of the string.
print(capitalized_text)  # Output: Python programming

# Another example:
sentence = "welcome to the jungle"
print(sentence.capitalize())  # Output: Welcome to the jungle


# ---------------------------
# Title Case (capitalize first letter of each word)
# ---------------------------
# Converting the first letter of each word to uppercase.
text = "hello world from python"
title_case_text = (
    text.title()
)  # Capitalizes the first character of each word in the string.
print(title_case_text)  # Output: Hello World From Python

# Another example:
movie_title = "the lord of the rings"
print(movie_title.title())  # Output: The Lord Of The Rings


# ---------------------------
# Swap Case (invert case of each letter)
# ---------------------------
# Inverting the case of all letters in the string.
text = "PyThOn Is AwEsOmE!"
swapped_case_text = (
    text.swapcase()
)  # Converts uppercase letters to lowercase and vice versa.
print(swapped_case_text)  # Output: pYtHoN iS aWeSoMe!

# Another example:
mixed_case = "HeLLo WoRLd"
print(mixed_case.swapcase())  # Output: hEllO wOrlD


# ---------------------------
# Replace a Substring
# ---------------------------
# Replacing a specific word in the string.
text = "I love Python"
replaced_text = text.replace(
    "Python", "JavaScript"
)  # Replaces occurrences of a substring with a new substring.
print(replaced_text)  # Output: I love JavaScript

# Another example:
greeting = "Hello, John"
new_greeting = greeting.replace("John", "Alice")  # Replaces 'John' with 'Alice'.
print(new_greeting)  # Output: Hello, Alice


# ---------------------------
# Split the String into a List
# ---------------------------
# Splitting the string into a list of words.
text = "Learn Python Programming"
split_list = text.split()  # Splits the string into a list at each space.
print(split_list)  # Output: ['Learn', 'Python', 'Programming']

# Another example (split using a comma):
csv_data = "name,age,city"
split_csv = csv_data.split(",")  # Splits the string at each comma.
print(split_csv)  # Output: ['name', 'age', 'city']


# ---------------------------
# Join a List into a String
# ---------------------------
# Joining a list of strings into a single string.
words = ["Python", "is", "fun"]
joined_string = " ".join(words)  # Joins the list elements into a string with spaces.
print(joined_string)  # Output: Python is fun

# Another example (joining with a hyphen):
word_list = ["easy", "to", "learn"]
joined_with_hyphen = "-".join(
    word_list
)  # Joins the list elements into a string with hyphens.
print(joined_with_hyphen)  # Output: easy-to-learn


# ---------------------------
# Strip Whitespace from Both Ends
# ---------------------------
# Removing leading and trailing whitespace from a string.
text = "   Hello World   "
stripped_text = text.strip()  # Removes whitespace from the start and end of the string.
print(stripped_text)  # Output: Hello World

# Another example (with extra newlines):
text_with_newlines = "\n   Welcome to Python!   \n"
clean_text = (
    text_with_newlines.strip()
)  # Removes whitespace and newlines from both ends.
print(clean_text)  # Output: Welcome to Python!


# ---------------------------
# Remove Leading Whitespace
# ---------------------------
# Removing whitespace from the start of the string (left side).
text = "   Python is cool"
left_stripped_text = (
    text.lstrip()
)  # Removes whitespace from the left side of the string.
print(left_stripped_text)  # Output: Python is cool

# Another example:
formatted_text = "     Data Science"
print(formatted_text.lstrip())  # Output: Data Science


# ---------------------------
# Check if the String is Titlecased
# ---------------------------
# Checking if each word in the string starts with an uppercase letter.
text = "Hello World"
is_title = (
    text.istitle()
)  # Checks if the string is titlecased (each word starts with an uppercase letter).
print(is_title)  # Output: True

# Another example:
sentence = "this is Not a Titlecased Sentence"
print(sentence.istitle())  # Output: False


# ---------------------------
# Check if the String Contains Only Whitespace
# ---------------------------
# Checking if the string consists only of whitespace.
text = "   "
contains_only_whitespace = (
    text.isspace()
)  # Checks if the string is made up of only whitespace characters.
print(contains_only_whitespace)  # Output: True

# Another example:
text_with_spaces = "   \n\t"
print(text_with_spaces.isspace())  # Output: True


# ---------------------------
# Check if All Characters are Digits
# ---------------------------
# Checking if all characters in the string are digits.
text = "12345"
are_digits = (
    text.isdigit()
)  # Checks if all characters in the string are numeric digits.
print(are_digits)  # Output: True

# Another example:
code = "A1234"
print(code.isdigit())  # Output: False


# ---------------------------
# Check if All Characters are Alphabetic
# ---------------------------
# Checking if all characters are alphabetic (letters only).
text = "HelloWorld"
are_alphabetic = (
    text.isalpha()
)  # Checks if all characters in the string are alphabetic.
print(are_alphabetic)  # Output: True

# Another example:
text_with_space = "Hello World"
print(text_with_space.isalpha())  # Output: False (contains space)


# ---------------------------
# Check if All Characters are Alphanumeric
# ---------------------------
# Checking if all characters are alphanumeric (letters and numbers).
text = "Python3"
are_alphanumeric = (
    text.isalnum()
)  # Checks if all characters in the string are either letters or numbers.
print(are_alphanumeric)  # Output: True

# Another example:
identifier = "123ABC"
print(identifier.isalnum())  # Output: True


# ---------------------------
# Count Occurrences of a Substring
# ---------------------------
# Counting the number of occurrences of a substring in the string.
text = "I love Python, Python is great"
python_count = text.count(
    "Python"
)  # Counts how many times 'Python' appears in the string.
print(python_count)  # Output: 2

# Another example:
sentence = "aaa bbb ccc aaa"
count_aaa = sentence.count("aaa")  # Counts how many times 'aaa' appears in the string.
print(count_aaa)  # Output: 2


# ---------------------------
# Find the Position of a Substring
# ---------------------------
# Finding the index of the first occurrence of a substring.
text = "I love Python"
position = text.find("Python")  # Finds the index of the first occurrence of 'Python'.
print(position)  # Output: 7

# Another example (substring not found):
not_found = text.find("Java")  # Returns -1 if the substring is not found.
print(not_found)  # Output: -1


# ---------------------------
# Check if String Ends with a Substring
# ---------------------------
# Checking if the string ends with the specified substring.
text = "file.txt"
ends_with_txt = text.endswith(".txt")  # Checks if the string ends with '.txt'.
print(ends_with_txt)  # Output: True

# Another example:
url = "https://example.com/"
print(url.endswith("/"))  # Output: True


# ---------------------------
# Check if String Starts with a Substring
# ---------------------------
# Checking if the string starts with the specified substring.
text = "Hello World"
starts_with_hello = text.startswith(
    "Hello"
)  # Checks if the string starts with 'Hello'.
print(starts_with_hello)  # Output: True

# Another example:
filename = "data.csv"
print(filename.startswith("data"))  # Output: True


# ---------------------------
# Capitalize Each Word in a Sentence
# ---------------------------
# Capitalizing the first letter of each word in a sentence.
text = "python is great for beginners"
capitalized_text = (
    text.title()
)  # Capitalizes the first letter of each word in the string.
print(capitalized_text)  # Output: Python Is Great For Beginners

# Another example:
quote = "live life to the fullest"
print(quote.title())  # Output: Live Life To The Fullest


# ---------------------------
# String Formatting (Using format())
# ---------------------------
# Using the format() method to insert values into a string.

name = "Bob"
age = 30

# Using the format() method to insert values into a string
formatted_string = "My name is {} and I am {} years old.".format(name, age)
# The curly braces {} are placeholders that will be replaced by the corresponding values in the format() method.
print(formatted_string)  # Output: My name is Bob and I am 30 years old.

# Another example using positional and keyword arguments:
# The indices {0} and {1} indicate the positions of the arguments in the format() method.
greeting = "Hello, {0}. You are {1} years old.".format(name, age)
print(greeting)  # Output: Hello, Bob. You are 30 years old.

# Using keyword arguments to insert values into the string
product = "laptop"  # String variable for product name
price = 899.99  # Float variable for product price
# The placeholders {product} and {price} correspond to the keyword arguments provided to format().
message = "The price of the {product} is ${price}.".format(product=product, price=price)
print(message)  # Output: The price of the laptop is $899.99.

# Formatting with fixed decimal places using the format() method
pi = 3.14159265  # Float variable holding the value of pi
# {:.2f} formats the float to two decimal places
formatted_pi = "Value of pi to two decimal places: {:.2f}".format(pi)
print(formatted_pi)  # Output: Value of pi to two decimal places: 3.14

# Formatting numbers with commas
number = 1000000  # Integer variable holding a large number
# {:,} formats the integer with commas as thousands separators
formatted_number = "Formatted number: {:,}".format(number)
print(formatted_number)  # Output: Formatted number: 1,000,000

# Formatting percentages
percentage = 0.75  # Float variable representing a fraction
# {:.2%} converts the float to a percentage format and displays it with two decimal places
formatted_percentage = "Completion: {:.2%}".format(percentage)
print(formatted_percentage)  # Output: Completion: 75.00%
