# ---------------------------
# Basic while loop
# ---------------------------
# A `while` loop repeatedly executes a block of code as long as a condition is `True`.

# Example: Print numbers from 1 to 5
number = 1

# The loop continues as long as `number` is less than or equal to 5.
while number <= 5:
    print(number)  # Output: 1, 2, 3, 4, 5
    number += 1  # Increment the number

# Explanation:
# - The loop condition is checked at the beginning of each iteration.
# - If the condition is `True`, the block inside the loop is executed.
# - The `number` variable is incremented to avoid an infinite loop.


# ---------------------------
# Infinite while loop
# ---------------------------
# A `while` loop without an exit condition can run infinitely.

# Example: Infinite loop (be careful when running this)
# while True:
#     print("This will run forever")

# Use case: Sometimes infinite loops are used when waiting for a user input or event to occur.


# ---------------------------
# Using break to exit a while loop
# ---------------------------
# The `break` statement exits the loop even if the condition is still `True`.

# Example: Stop the loop when number equals 3
number = 1
while number <= 5:
    if number == 3:
        break  # Exit the loop when number is 3
    print(number)  # Output: 1, 2
    number += 1

# Explanation:
# - The loop prints numbers 1 and 2, but stops when `number` equals 3 due to the `break` statement.


# ---------------------------
# Using continue to skip an iteration
# ---------------------------
# The `continue` statement skips the rest of the current iteration and goes to the next one.

# Example: Skip printing number 3
number = 1
while number <= 5:
    number += 1
    if number == 3:
        continue  # Skip the rest of the code when number is 3
    print(number)  # Output: 2, 4, 5, 6

# Explanation:
# - The `continue` statement skips printing when `number` is 3.
# - It proceeds to the next iteration without executing the rest of the loop.


# ---------------------------
# while with else
# ---------------------------
# The `else` block executes after the loop finishes, unless the loop is terminated by `break`.

# Example: Print numbers with an else clause
number = 1
while number <= 3:
    print(number)  # Output: 1, 2, 3
    number += 1
else:
    print("Loop is finished.")  # Output: Loop is finished.

# Explanation:
# - The `else` block runs after the loop completes normally (without a `break`).
# - It's useful for handling tasks once the loop finishes.


# ---------------------------
# Nested while loop
# ---------------------------
# A `while` loop can also be nested inside another loop.

# Example: Multiplication table using nested while loops
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"{i} * {j} = {i * j}")
        j += 1
    i += 1
# Output:
# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
# 2 * 1 = 2
# 2 * 2 = 4
# 2 * 3 = 6
# 3 * 1 = 3
# 3 * 2 = 6
# 3 * 3 = 9

# Explanation:
# - The outer loop controls the row, while the inner loop controls the column.
# - The `j` loop resets to 1 after each outer loop iteration.


# ---------------------------
# Use case: Input validation with while loop
# ---------------------------
# `while` loops are often used to repeatedly ask for valid input from the user.

# Example: Keep asking for input until a valid age is entered
age = -1

# The loop continues until a valid age is entered (positive number).
while age < 0:
    age = int(input("Enter your age (must be positive): "))
    if age < 0:
        print("Invalid input. Age cannot be negative.")

print(f"Your age is {age}.")  # Output: Your age is [entered age].

# Explanation:
# - The loop continues to ask for input as long as the entered age is negative.
# - When a valid (positive) age is entered, the loop ends.


# ---------------------------
# Use case: Countdown timer
# ---------------------------
# A common use for `while` loops is a countdown timer.

# Example: Countdown from 5 to 1
countdown = 5
while countdown > 0:
    print(f"Countdown: {countdown}")
    countdown -= 1  # Decrease the counter
print("Blast off!")  # Output: Blast off!

# Explanation:
# - The loop counts down from 5 to 1.
# - Once the countdown reaches 0, the loop stops, and the final message is printed.


# ---------------------------
# Use case: Simulating user login attempts
# ---------------------------
# A `while` loop can be used to simulate multiple user login attempts.

# Example: Allow 3 attempts to enter the correct password
password = "secret"
attempts = 3

while attempts > 0:
    user_input = input("Enter password: ")
    if user_input == password:
        print("Login successful!")  # Output when correct password is entered.
        break
    else:
        attempts -= 1
        print(f"Incorrect password. {attempts} attempts left.")
else:
    print("Account locked.")  # Output if all attempts are exhausted.

# Explanation:
# - The user has 3 chances to enter the correct password.
# - If the correct password is entered, the loop ends with a successful login.
# - If all attempts are used up, the account is locked.
