x = 10

# ---------------------------
# Logical AND
# ---------------------------
# Returns True if both operands are true.
and_result = (x > 5) and (x < 10)
print(f"Logical AND: {and_result}")  # Output: True

# ---------------------------
# Logical OR
# ---------------------------
# Returns True if at least one of the operands is true.
or_result = (x < 5) or (x < 10)
print(f"Logical OR: {or_result}")  # Output: True

# ---------------------------
# Logical NOT
# ---------------------------
# Reverses the logical state of its operand.
not_result = not (x > 5)
print(f"Logical NOT: {not_result}")  # Output: False
