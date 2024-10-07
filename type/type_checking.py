# ---------------------------
# Check for Boolean Type
# ---------------------------
# To check if a variable is of boolean type, we can use the isinstance() function.

bool_value = True  # Example boolean value

# Check for boolean type
is_bool = isinstance(bool_value, bool)  # Returns True if bool_value is a boolean

print(f"Is bool_value a boolean? {is_bool}")  # Output: Is bool_value a boolean? True
print(
    f"The type of bool_value is: {type(bool_value)}"
)  # Output: The type of bool_value is: <class 'bool'>

# ---------------------------
# Check for Mapping Type
# ---------------------------
# To check if a variable is a mapping type (dictionary), we use the isinstance() function.

dict_example = {"name": "Alice", "age": 30}  # Example dictionary

# Check for mapping type
is_mapping = isinstance(
    dict_example, dict
)  # Returns True if dict_example is a dictionary

print(
    f"Is dict_example a mapping type? {is_mapping}"
)  # Output: Is dict_example a mapping type? True
print(
    f"The type of dict_example is: {type(dict_example)}"
)  # Output: The type of dict_example is: <class 'dict'>

# ---------------------------
# Check for None Type
# ---------------------------
# To check if a variable is of None type, we can use the is keyword or isinstance() function.

none_value = None  # Example None value

# Check for None type
is_none = none_value is None  # Returns True if none_value is None

print(f"Is none_value None? {is_none}")  # Output: Is none_value None? True
print(
    f"The type of none_value is: {type(none_value)}"
)  # Output: The type of none_value is: <class 'NoneType'>

# ---------------------------
# Check for Numeric Types
# ---------------------------
# To check if a variable is a numeric type, we can use isinstance() with int, float, or complex.

int_value = 42  # Example integer
float_value = 3.14  # Example float
complex_value = 2 + 3j  # Example complex number

# Check for numeric types
is_int = isinstance(
    int_value, (int, float, complex)
)  # Returns True if int_value is numeric
is_float = isinstance(
    float_value, (int, float, complex)
)  # Returns True if float_value is numeric
is_complex = isinstance(
    complex_value, (int, float, complex)
)  # Returns True if complex_value is numeric

print(f"Is int_value numeric? {is_int}")  # Output: Is int_value numeric? True
print(
    f"The type of int_value is: {type(int_value)}"
)  # Output: The type of int_value is: <class \'int\'>'
print(f"Is float_value numeric? {is_float}")  # Output: Is float_value numeric? True
print(
    f"The type of float_value is: {type(float_value)}"
)  # Output: The type of float_value is: <class \'float\'>'
print(
    f"Is complex_value numeric? {is_complex}"
)  # Output: Is complex_value numeric? True
print(
    f"The type of complex_value is: {type(complex_value)}"
)  # Output: The type of complex_value is: <class \'complex\'>

# ---------------------------
# Check for Sequence Types
# ---------------------------
# To check if a variable is a sequence type (list, tuple, or range), we can use isinstance().

list_example = [1, 2, 3]  # Example list
tuple_example = (1, 2, 3)  # Example tuple
range_example = range(5)  # Example range

# Check for sequence types
is_list = isinstance(
    list_example, (list, tuple, range)
)  # Returns True if list_example is a sequence
is_tuple = isinstance(
    tuple_example, (list, tuple, range)
)  # Returns True if tuple_example is a sequence
is_range = isinstance(
    range_example, (list, tuple, range)
)  # Returns True if range_example is a sequence

print(
    f"Is list_example a sequence? {is_list}"
)  # Output: Is list_example a sequence? True
print(
    f"The type of list_example is: {type(list_example)}"
)  # Output: The type of list_example is: <class \'list\'>'
print(
    f"Is tuple_example a sequence? {is_tuple}"
)  # Output: Is tuple_example a sequence? True
print(
    f"The type of tuple_example is: {type(tuple_example)}"
)  # Output: The type of tuple_example is: <class \'tuple\'>'
print(
    f"Is range_example a sequence? {is_range}"
)  # Output: Is range_example a sequence? True
print(
    f"The type of range_example is: {type(range_example)}"
)  # Output: The type of range_example is: <class \'range\'>

# ---------------------------
# Check for Set Types
# ---------------------------
# To check if a variable is a set type, we use the isinstance() function.

set_example = {1, 2, 3}  # Example set

# Check for set types
is_set = isinstance(set_example, set)  # Returns True if set_example is a set

print(f"Is set_example a set? {is_set}")  # Output: Is set_example a set? True
print(
    f"The type of set_example is: {type(set_example)}"
)  # Output: The type of set_example is: <class \'set\'>

# ---------------------------
# Check for String Type
# ---------------------------
# To check if a variable is of string type, we use the isinstance() function.

string_value = "Hello, World!"  # Example string

# Check for string type
is_string = isinstance(string_value, str)  # Returns True if string_value is a string

print(
    f"Is string_value a string? {is_string}"
)  # Output: Is string_value a string? True
print(
    f"The type of string_value is: {type(string_value)}"
)  # Output: The type of string_value is: <class \'str\'>'
