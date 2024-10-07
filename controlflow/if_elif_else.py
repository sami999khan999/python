# ---------------------------
# if
# ---------------------------
# `if` statements check if a condition is True, and if so, execute a block of code.

# Check if a number is positive
number = 5

# If the number is greater than 0, it's positive.
if number > 0:
    print("The number is positive.")  # Output: The number is positive.

# Explanation:
# - The `if` statement checks if the value of `number` is greater than 0.
# - If True, the code inside the `if` block runs and prints the message.
# - If the condition were False, nothing would be printed since there is no `else` block.

# ---------------------------
# if else
# ---------------------------
# `if else` allows for an alternate block of code to execute if the `if` condition is False.

# Determine if a student passed or failed
score = 75

# If the student's score is 60 or higher, they pass. Otherwise, they fail.
if score >= 60:
    print("Student passed.")  # Output: Student passed.
else:
    print("Student failed.")

# Explanation:
# - The `if` statement checks if the score is 60 or higher.
# - If the condition is True, the "Student passed." message is printed.
# - If False, the `else` block runs, printing "Student failed."

# Determine a student's grade based on their score
score = 85

# If the student's score is 90 or above, they get an A. Otherwise, they get a B.
if score >= 90:
    print("Grade: A")
else:
    print("Grade: B")  # Output: Grade: B.

# Explanation:
# - This `if else` statement checks for two conditions.
# - If the score is 90 or higher, the "Grade: A" message is printed.
# - If the score is below 90, the `else` block runs, printing "Grade: B".

# ---------------------------
# if elif else
# ---------------------------
# `elif` (else if) allows for multiple conditions to be checked one after another.

# Determine the letter grade of a student
score = 72

# Multiple conditions to check for A, B, C, or F grades based on the score.
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")  # Output: Grade: C.
else:
    print("Grade: F")

# Explanation:
# - The `if` checks if the score is 90 or above for an A grade.
# - If the first condition is False, it moves to the `elif` to check if the score is 80 or higher for a B.
# - If both conditions are False, the next `elif` checks if the score is 70 or higher for a C.
# - If none of the conditions are True, the `else` block runs and prints "Grade: F."

# Determine a student's performance level based on score ranges
score = 55

# Checking for different performance levels based on score ranges.
if score >= 90:
    print("Excellent")
elif score >= 75:
    print("Good")
elif score >= 50:
    print("Satisfactory")  # Output: Satisfactory.
else:
    print("Needs Improvement")

# Explanation:
# - This code checks four conditions in a sequence.
# - The `if` checks if the score is 90 or above for "Excellent".
# - The `elif` checks for scores between 75 and 89 for "Good".
# - Another `elif` checks for scores between 50 and 74 for "Satisfactory".
# - If none of these are True, the `else` block runs, meaning the score is below 50, printing "Needs Improvement."

# ---------------------------
# nested if
# ---------------------------
# Nested `if` statements allow checking multiple conditions within an `if` block.

# Check if a number is positive and even
number = 4

# The first `if` checks if the number is positive.
if number > 0:
    # Inside the first `if`, we check if the number is even.
    if number % 2 == 0:
        print(
            "The number is positive and even."
        )  # Output: The number is positive and even.

# Explanation:
# - First, the outer `if` checks if the number is greater than 0 (positive).
# - If True, the nested `if` inside checks if the number is divisible by 2 (even).
# - If both conditions are True, it prints "The number is positive and even."

# Check if a person is eligible to vote based on age and citizenship
age = 20
citizenship = True

# The first `if` checks if the person is 18 or older (age eligibility).
if age >= 18:
    # Inside the first `if`, we check if the person is a citizen.
    if citizenship:
        print("Eligible to vote.")  # Output: Eligible to vote.
    else:
        print("Not a citizen, cannot vote.")
else:
    print("Not old enough to vote.")

# Explanation:
# - The outer `if` checks if the person is 18 or older (legal voting age).
# - Inside this block, another `if` checks if the person is a citizen.
# - If both conditions are True, it prints "Eligible to vote."
# - If they are not a citizen, it prints "Not a citizen, cannot vote."
# - If the person is younger than 18, the outer `else` block prints "Not old enough to vote."
