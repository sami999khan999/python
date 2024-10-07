# ---------------------------
# is
# ---------------------------
# Returns True if two variables point to the same object in memory.
a = [1, 2, 3]
b = a
is_same_object = a is b
print(f"Is: {is_same_object}")  # Output: True

# ---------------------------
# is not
# ---------------------------
# Returns True if two variables do not point to the same object in memory.
c = [1, 2, 3]
is_not_same_object = a is not c
print(f"Is Not: {is_not_same_object}")  # Output: True
