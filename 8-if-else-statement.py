# if-else statement

# The if-else statement in Python is used to perform conditional logic, allowing your program to make decisions based on certain conditions.

# The condition in an if statement can be any expression that evaluates to True or False.
# Python uses indentation (spaces or tabs) to define the blocks of code under if, elif, and else.
# You can have as many elif statements as needed, but only one else statement.

age = int(input("How old are you?"))

if age >= 18:
  print("You are an adult.")
elif age <= 0:
  print("You haven't been bord yet.")
else:
  print("You are a child.")