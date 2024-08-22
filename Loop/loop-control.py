# loop control

# Loop control statements in Python alter the normal flow of execution of loops (for and while). These statements allow you to control when to exit a loop or skip an iteration. The primary loop control statements in Python are break, continue, and pass.

# ===================================================================================================== #

# break

# The break statement is used to exit a loop prematurely, even if the loop's condition is still True.

while True:
    name = input("Enter yout name: ")
    if name != "":
        break

for i in range(1, 10 + 1):
    if i == 8:
        break
    print(i)

# ===================================================================================================== #

# continue

# The continue statement is used to skip the rest of the code inside the loop for the current iteration and move to the next iteration.

phone_number = "123-456-789"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

# ===================================================================================================== #

# pass

# The pass statement does nothing. It is a placeholder used when a statement is required syntactically but you don't want to execute any code.

for i in range(5):
    if i == 3:
        pass
    print(i)
