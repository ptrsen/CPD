# Sets: unorder collection of unique objects
print("\nPython - Sets ")
my_set = {1, 2, 3, 4, 5, 5} # there is no duplicates
my_set.add(100)
my_set.add(2)
print(my_set) # duplicates are not added, ex. 5

my_list = [1, 2, 3, 4, 4, 5, 5]
print(set(my_list)) # convert to a new set, useful when we want to remove duplicates
print(list(my_set)) # convert to a new list

# my_set[1] # Error we can not get values in sets
print(1 in my_set)

new_set = my_set.copy()
my_set.clear()
print(my_set)
print(new_set)



# Set Methods, as venn diagrams to compare two sets
print("\nSet - Methods ")
my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

print(my_set.difference(your_set)) # get the differences between two sets
print(my_set.intersection(your_set)) # get intersection between two sets
print(my_set.isdisjoint(your_set)) # 
print(my_set.issubset(your_set)) #
print(my_set.issuperset(your_set)) #
print(my_set.union(your_set)) #
my_set.difference_update(your_set) #
print(my_set) 
my_set.discard(5)
print(my_set)