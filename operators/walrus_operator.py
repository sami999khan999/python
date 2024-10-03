# Walrus Operator (:=):
# The Walrus operator (:=) is used to assign values to variables as part of an expression.
# It was introduced in Python 3.8 and allows assignment and evaluation in a single step,
# making the code more concise in some scenarios, especially within loops and conditionals.

# Example 1: Assigning and printing 'alive' variable using the walrus operator
# The walrus operator assigns the value True to the variable 'alive' and immediately prints it.
print(alive := 6)  # Output: True


# Example 2: Using the walrus operator inside a while loop
# 'food := input()' allows us to capture the user input and compare it to "quit" in one line.
# The loop continues as long as the input isn't "quit".
foods = []

# The walrus operator is used within the while condition to assign the user input to 'food'
# and also check whether it's "quit". If it's not, the loop continues and the food is appended to 'foods' list.
while (food := input("What food do you want to eat? ")) != "quit":
    foods.append(food)

# After the loop ends (when user enters "quit"), the collected foods are printed.
print(foods)

# Key Points:
# 1. The walrus operator (:=) allows assignment and condition evaluation in one expression.
# 2. This operator is especially useful in loops where we need to both assign and check a value.
# 3. In the while loop example, it avoids the need for a separate assignment step before the condition.
