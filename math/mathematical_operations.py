import math  # Importing the math module for advanced mathematical functions

# ---------------------------
# Square Root
# ---------------------------
# Define a number to find its square root.
number_for_sqrt = 16
# Calculate the square root of the specified number.
square_root_result = math.sqrt(number_for_sqrt)
print("Square Root:", square_root_result)  # Output: Square Root: 4.0


# ---------------------------
# Power
# ---------------------------
# Define the base and exponent for the power calculation.
base = 2
exponent = 5
# Calculate the result of raising the base to the exponent.
power_result = math.pow(base, exponent)
print("Power:", power_result)  # Output: Power: 32.0


# ---------------------------
# Trigonometric Functions
# ---------------------------
# Define an angle in degrees for trigonometric calculations.
angle_degrees = 30
# Convert the angle to radians for the math functions.
angle_radians = math.radians(angle_degrees)
# Calculate the sine of the angle.
sine_result = math.sin(angle_radians)
print("Sine:", sine_result)  # Output: Sine: 0.49999999999999994

# Calculate the cosine of the angle.
cosine_result = math.cos(angle_radians)
print("Cosine:", cosine_result)  # Output: Cosine: 0.8660254037844387

# Calculate the tangent of the angle.
tangent_result = math.tan(angle_radians)
print("Tangent:", tangent_result)  # Output: Tangent: 0.5773502691896257


# ---------------------------
# Logarithmic Functions
# ---------------------------
# Define a number for logarithmic calculations.
number_for_log = 100
# Calculate the natural logarithm (base e) of the number.
natural_log_result = math.log(number_for_log)
print(
    "Natural Logarithm:", natural_log_result
)  # Output: Natural Logarithm: 4.605170185988092

# Calculate the base 10 logarithm of the number.
log10_result = math.log10(number_for_log)
print("Base 10 Logarithm:", log10_result)  # Output: Base 10 Logarithm: 2.0


# ---------------------------
# Factorial
# ---------------------------
# Define a number to calculate its factorial.
factorial_number = 5
# Calculate the factorial of the specified number.
factorial_result = math.factorial(factorial_number)
print("Factorial:", factorial_result)  # Output: Factorial: 120


# ---------------------------
# Greatest Common Divisor (GCD)
# ---------------------------
# Define two numbers to find their GCD.
num1_for_gcd = 48
num2_for_gcd = 18
# Calculate the GCD of the two specified numbers.
gcd_result = math.gcd(num1_for_gcd, num2_for_gcd)
print("Greatest Common Divisor:", gcd_result)  # Output: Greatest Common Divisor: 6


# ---------------------------
# Absolute Value
# ---------------------------
# Define a negative number to find its absolute value.
negative_number = -42
# Calculate the absolute value of the specified number.
absolute_value_result = abs(negative_number)
print("Absolute Value:", absolute_value_result)  # Output: Absolute Value: 42


# ---------------------------
# Floor and Ceiling
# ---------------------------
# Define a floating-point number for floor and ceiling calculations.
float_number = 5.7
# Calculate the largest integer less than or equal to the float_number.
floor_result = math.floor(float_number)
print("Floor:", floor_result)  # Output: Floor: 5

# Calculate the smallest integer greater than or equal to the float_number.
ceiling_result = math.ceil(float_number)
print("Ceiling:", ceiling_result)  # Output: Ceiling: 6


# ---------------------------
# Constants
# ---------------------------
# Get the value of the mathematical constant pi.
pi_value = math.pi
print("Value of Pi:", pi_value)  # Output: Value of Pi: 3.141592653589793

# Get the value of the mathematical constant e (Euler's number).
e_value = math.e
print("Value of e:", e_value)  # Output: Value of e: 2.718281828459045
