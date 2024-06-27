# Tuples
# same as list but cannot be change , they are unmmutable
print("\nPython - Tuples ")
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1]) # get index 1
# my_tuple[1] = 5 # ERROR is unmutable

print(5 in my_tuple) # find if 5 is in tuple
print(my_tuple) # print all tuple


# Slicing same as lists, but remember return also a tuple
print("\nTuples - Slicing ")
print(my_tuple[1:2])  # get index 1
print(my_tuple[::-1]) 

x, y, z, *other = (1, 2, 3, 4, 5) # also as list we can assing different things 
print(x)
print(z)

# Methods
print("\nTuples - methods ")
print(my_tuple.count(5)) # get number of time 5 is found in tuple
print(my_tuple.index(5)) # get index 5
print(len(my_tuple)) # lenght