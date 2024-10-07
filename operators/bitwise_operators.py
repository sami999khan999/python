# ---------------------------
# Bitwise AND
# ---------------------------
# Compares each bit of two numbers; if both bits are 1, the result is 1.
bitwise_and_result = 5 & 3  # Binary: 0101 & 0011 = 0001 (1)
print(f"Bitwise AND: {bitwise_and_result}")  # Output: 1

# ---------------------------
# Bitwise OR
# ---------------------------
# Compares each bit of two numbers; if at least one bit is 1, the result is 1.
bitwise_or_result = 5 | 3  # Binary: 0101 | 0011 = 0111 (7)
print(f"Bitwise OR: {bitwise_or_result}")  # Output: 7

# ---------------------------
# Bitwise NOT
# ---------------------------
# Reverses all bits of the operand.
bitwise_not_result = ~5  # Binary: ~0101 = 1010 (-6)
print(f"Bitwise NOT: {bitwise_not_result}")  # Output: -6

# ---------------------------
# Bitwise XOR
# ---------------------------
# Compares each bit of two numbers; if the bits are different, the result is 1.
bitwise_xor_result = 5 ^ 3  # Binary: 0101 ^ 0011 = 0110 (6)
print(f"Bitwise XOR: {bitwise_xor_result}")  # Output: 6

# ---------------------------
# Bitwise Shift Left
# ---------------------------
# Shifts the bits of a number to the left by a specified number of positions.
bitwise_shift_left_result = 5 << 1  # Binary: 0101 << 1 = 1010 (10)
print(f"Bitwise Shift Left: {bitwise_shift_left_result}")  # Output: 10

# ---------------------------
# Bitwise Shift Right
# ---------------------------
# Shifts the bits of a number to the right by a specified number of positions.
bitwise_shift_right_result = 5 >> 1  # Binary: 0101 >> 1 = 0010 (2)
print(f"Bitwise Shift Right: {bitwise_shift_right_result}")  # Output: 2
