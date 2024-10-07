# ---------------------------
# Logical Operators in Python
# ---------------------------
# Logical operators are used to combine conditional statements.
# - `and`: Returns True if both conditions are True.
# - `or`: Returns True if at least one condition is True.
# - `not`: Reverses the result, returning False if the result is True and vice versa.

# ---------------------------
# Using 'and' with if, elif, else
# ---------------------------
# Example: Check if a person is eligible to vote and a citizen
age = 25
citizenship = True

if age >= 18 and citizenship:
    print("Eligible to vote.")  # Output: Eligible to vote.
else:
    print("Not eligible to vote.")

# Explanation:
# - The `and` operator ensures both conditions (`age >= 18` and `citizenship`) must be True.
# - If either condition is False, the person is not eligible to vote.


# ---------------------------
# Using 'or' with if, elif, else
# ---------------------------
# Example: Check if a person can qualify for a discount based on age or membership
age = 17
is_member = True

if age < 18 or is_member:
    print("Eligible for a discount.")  # Output: Eligible for a discount.
else:
    print("Not eligible for a discount.")

# Explanation:
# - The `or` operator allows the person to qualify for a discount if either condition is True.
# - If at least one of the conditions (`age < 18` or `is_member`) is True, the discount applies.


# ---------------------------
# Using 'not' with if, elif, else
# ---------------------------
# Example: Check if a number is NOT positive
number = -3

if not number > 0:
    print("The number is not positive.")  # Output: The number is not positive.
else:
    print("The number is positive.")

# Explanation:
# - The `not` operator reverses the result of the condition (`number > 0`).
# - Since the number is negative, the `not` operator makes the condition True, and the message is printed.


# ---------------------------
# Combining 'and' and 'or' in if, elif, else
# ---------------------------
# Example: Determine admission eligibility based on age, test score, or special status
age = 17
test_score = 85
special_status = False

if (age >= 18 and test_score >= 80) or special_status:
    print("Eligible for admission.")  # Output: Eligible for admission.
else:
    print("Not eligible for admission.")

# Explanation:
# - The `and` operator checks that both age and test score meet the criteria.
# - The `or` operator allows the person to qualify if they have special status, even if other conditions aren't met.


# ---------------------------
# if elif else with logical operators
# ---------------------------
# Example: Determine discount based on various conditions
age = 17
is_student = True
has_membership = False

if age < 18 or is_student:
    print("Eligible for student discount.")  # Output: Eligible for student discount.
elif has_membership and age >= 18:
    print("Eligible for membership discount.")
else:
    print("No discount available.")

# Explanation:
# - The `or` operator checks if the person is either under 18 or a student for a discount.
# - The `elif` block uses `and` to give a discount only if the person is a member and over 18.


# ---------------------------
# Complex conditions using logical operators
# ---------------------------
# Example: Check multiple conditions for driving license eligibility
age = 18
has_license = True
good_vision = False

if age >= 18 and has_license and good_vision:
    print("Eligible to drive.")
elif age >= 18 and (has_license or good_vision):
    print("Partially eligible for restricted driving.")
else:
    print("Not eligible to drive.")  # Output: Not eligible to drive.

# Explanation:
# - The first condition ensures that the person meets all the criteria for driving.
# - The second `elif` condition checks partial eligibility if they meet only one of the two criteria (`has_license` or `good_vision`).
# - If neither condition is met, the `else` block states that they are not eligible to drive.


# ---------------------------
# Use case: Checking user permissions
# ---------------------------
# Example: Determine user access level based on role and status
is_admin = False
is_moderator = True
is_active = True

if is_admin and is_active:
    print("Access granted with admin privileges.")
elif is_moderator and is_active:
    print(
        "Access granted with moderator privileges."
    )  # Output: Access granted with moderator privileges.
else:
    print("Access denied.")

# Explanation:
# - The `and` operator ensures that the user is both an admin or moderator and their account is active.
# - If neither condition is met, access is denied.


# ---------------------------
# Use case: Validating input ranges
# ---------------------------
# Example: Check if a number falls within multiple ranges
number = 45

if 0 <= number <= 50:
    print(
        "Number is within the range 0-50."
    )  # Output: Number is within the range 0-50.
elif 51 <= number <= 100:
    print("Number is within the range 51-100.")
else:
    print("Number is outside the range.")

# Explanation:
# - The condition `0 <= number <= 50` checks if the number is in the range from 0 to 50.
# - The `elif` block checks the next range, and the `else` handles out-of-range numbers.


# ---------------------------
# Use case: Multiple conditions for discount eligibility
# ---------------------------
# Example: Determine a customer’s discount eligibility based on multiple factors
age = 25
is_student = False
has_coupon = True
total_purchase = 150

if total_purchase >= 100 and (age < 18 or is_student or has_coupon):
    print("Eligible for a discount.")  # Output: Eligible for a discount.
else:
    print("Not eligible for a discount.")

# Explanation:
# - The `and` operator ensures that the total purchase is $100 or more.
# - The `or` operator checks if the person qualifies for a discount by being under 18, a student, or having a coupon.
