# nested loop

# A nested loop is a loop inside another loop. The inner loop runs completely for each iteration of the outer loop. Nested loops are useful when you need to perform complex iterations over multi-dimensional data structures like lists of lists, grids, or matrices.

# ===================================================================================================== #

rows = int(input("How many rows? "))
columns = int(input("How many columns? "))
symbol = input("Symbol? ")

for i in range(rows):
  for j in range(columns):
    print(symbol, end="")
  print() 