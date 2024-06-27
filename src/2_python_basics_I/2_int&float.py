# Integers (int) and Floating point (float) numbers
print("\nPython - Numbers: ")
print('int: ', 42) 
print('int: ', -42) # Negative int
print('float: ', 3.14)
print('float: ', -3.14) # Negative float

# Numbers operations
print("\nPython - Numbers Operations: ")
print(2 + 4) # Addition
print(2.5 - 4) # Substraction 
print(2 * 4) # Multiplication
print(2 / 4) # Division
print(2 ** 3) # Exponential: 2^3
print(5 // 4) # Integer division rounded down, always return int
print(5 % 4)  # Modulo: return the division remainer 

# Find types
print("\nPython - Numbers Types: ")
print(type(2 * 4)) # return int 
print(type(2 / 4)) # return float
print(type(2.5 + 4)) # return float

# Some math functions: Actions to perform with numbers
print("\nPython - Some Math functions: ")
print(round(3.1)) # round number to nearest integer 
print(round(3.9)) # round number to nearest integer 
print(abs(3.9)) # absolute value (always return positive numbers) 
print(abs(-3.9))   

# Operator precendence (mathematics) 
print("\nPython - Operator precendence: ")
# Order of operation: 
# 1. Parenthesis () 
# 2. Exponential (**) 
# 3. Multiplication (*) or Division (/) 
# 4. Addition (+) or Substraction (-)
print((20 - 3) + 2 ** 2)

# Others
print("\nPython - Other numbers ")
# Complex Numbers
complex() 
# Binary numbers
print(bin(5)) # convert integer 5 to binary (base 2)
print(int("0b101", 2)) # convert binary 0b101 to integer, ("number", base of number)