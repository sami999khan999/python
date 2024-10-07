# ---------------------------
# Operator Precedence
# ---------------------------
# Operator precedence determines the order in which operations are performed
# in an expression. Higher precedence operators are evaluated before lower
# precedence ones. This is crucial for ensuring that expressions produce
# the intended results.

# The general order of precedence (from highest to lowest) is as follows:
# 1. Parentheses ()
# 2. Exponents ** (power)
# 3. Unary plus and minus (+x, -x)
# 4. Multiplication and Division (*, /, //, %)
# 5. Addition and Subtraction (+, -)
# 6. Bitwise AND (&)
# 7. Bitwise XOR (^)
# 8. Bitwise OR (|)

# ---------------------------
# Examples
# ---------------------------

# Example 1: Using parentheses to alter precedence
result1 = 2 + 3 * 4  # Output: 14 (Multiplication first)
result2 = (2 + 3) * 4  # Output: 20 (Addition first due to parentheses)

# Example 2: Exponentiation takes precedence over multiplication
result3 = 2 * 3**2  # Output: 18 (3 squared first)
result4 = (2 * 3) ** 2  # Output: 36 (Multiplication first due to parentheses)

# Example 3: Mixed operators
result5 = 5 + 2 * 3 - 1  # Output: 10 (2 * 3 = 6, then 5 + 6 - 1)
result6 = (5 + 2) * (
    3 - 1
)  # Output: 14 (Both operations inside parentheses are calculated first)

# Example 4: Division and multiplication
result7 = 8 / 4 * 2  # Output: 4.0 (Division first, then multiplication)

# Example 5: Unary operators
number = -3
result8 = -number + 5  # Output: 8 (Unary minus takes precedence)

# It is always a good practice to use parentheses to make expressions clear
# and to avoid ambiguity, even if the precedence rules would yield the
# correct result.
