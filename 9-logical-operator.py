# logical operator

# Logical operators are used to combine conditional statements and evaluate boolean expressions. They return True or False based on the evaluation of the conditions they operate on. Python supports three primary logical operators: and, or, and not.

temp = int(input("What is the temperature outside?"))

# ===================================================================================================== #

# AND operator

# The AND operator returns True if both operands are True. Otherwise, it returns False.

# if temp >= 0  and temp <=30:
#   print("It's warm outside.")
# elif temp < 0 and temp >= -20:
#   print("It's cold outside.")
# else:
#   print("Don't go outside")

# ===================================================================================================== #

# OR operator

# The OR operator returns True if either of the operands is True. Otherwise, it returns False.

if temp >= 0 or temp >= 200: 
  print("It's warm outside.")
else:
  print("It's cold outside.")

# ===================================================================================================== #

# NOT operator

# The NOT operator returns True if the operand is False and False if the operand is True.

if not(temp >=0):
  print("it's warm outside.")
elif not(temp <= -20):
  print("it's cold outside.")
else:
  print("Don't go outside")