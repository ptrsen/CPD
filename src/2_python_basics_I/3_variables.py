# Variables: store information in memory
# Python:
# - Star with lowercase or underscore (for private varibles)
# - Can have Letters, numbers, undersscore
# - Case sensitive
# - Don't overwrite keywords
# - Example: snake_case

print("\nPython - Variables ")

a = 190 # assign (also called binding) 190 to var 'a'
print("Variable a = ", a) 

# Multiple assigments 
a, b ,c = 1, 2, "hello"
print("Variable a = ", a) 
print("Variable b = ", b) 
print("Variable c = ", c) 

# Expression vs Statements
apple_price = 5.5    #( 1 statement)
banana_price = 6.5   #( 2 statement)
# I buy 2 apples and 2 bananas
total_price = (2*apple_price) + (2*banana_price) #( formula is and expression)
print("total price: ", total_price) 


# Augmented Assigment operator
a = 5
a = a + 5
print(a)
# latest can be replace with te augmented operator
a = 5
a += 5
print(a)
a -= 5
print(a)




