# Lists: order squence of objects of any type. lists in python are like arrays in other languages
print("\nPython - Lists ")
li = [1, 2, 3, 4, 5] # list of numbers
print(li)
li2 = ['a', 'b', 'c'] # list of characters
print(li2)
li3 = [1, 2.5, 'a', True] # list of different values
print(li3)

amazon_cart = ['notebooks', 'sunglasses']
print(amazon_cart[0]) # accesing index 0 of list
print('\n')


# List Slicing: same as strings
# [Start : Stop : Step-Over]
print("\nPython - List Slicing ")
amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes']
print(amazon_cart) # all list
print(amazon_cart[0:2]) # 'notebooks', 'sunglasses'
print(amazon_cart[0::2]) # 'notebooks', 'toys'
print(amazon_cart[::-1]) # reverse


# Lists are mutable
print("\nPython - List mutable ")
amazon_cart[0] = 'laptop'
print(amazon_cart)

# Every time we do list slicing we create a new list copy  
new_cart = amazon_cart[:]
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

new_cart1 = amazon_cart
new_cart1[0] = 'gum'
print(new_cart1)
print(amazon_cart)
print('\n')


# Matrix: multidimensional lists , 2D for example
print("\nPython - List as Matrix ")
matrix = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]
print(matrix)
print(matrix[0][2])


# List Methods
print("\nPython - List Methods ")
basket = [1, 2, 3, 4, 5]
print(basket)
print(len(basket)) # length

# Adding
print('\n Adding')
new_list = basket.append(100) # append did not create a new list
print(new_list) # print none
basket.insert(4, 50) # add 50 in index 4, did not create a new list
print(basket)
basket.extend([10, 20, 30, 40])
print(basket)

# Removing
print('\n Removing')
basket.pop()
print(basket)
basket.pop(4)
print(basket)
basket.remove(100)
print(basket)
# basket.clear()
# print(basket)

print('\n Index and Count methods')
print(basket.index(5)) # get index
print(5 in basket) # python keyboard 'in', search if 5 is in list and return true or false
print(basket.count(4)) # count how many times 4 is in basket

print('\n Sort, Copy , Reverse methods')
basket.sort()  # sort list
print(basket) 
new_basket = basket.copy() # make a copy
new_basket.sort(reverse=True) # sort in reverse order
print(new_basket)
print(sorted(new_basket)) # sorted function produces a new list, not like .sort() method
basket.reverse()
print(basket)


# Common List Patterns
print('\n List Patterns')
print(basket[::-1]) # reverse with list slicing, creates a new list
print(range(1, 100)) # print range from 1 to 100
print(list(range(101))) # generate a list from 1 to 100

sentence = '! '
new_sentence = sentence.join(['Hi', 'my', 'name', 'is', 'JOJO']) # join take iterable (list 'sentence') and join '!' with every element 
print(new_sentence)


# List Unpacking
print('\nList Unpacking')
a, b, c, *other, d, e = [1, 2, 3, 4, 5, 6, 7, 8, 9] # assing each element of list to each variable
print(a)
print(b)
print(c)
print(other) #  keeps rest of the list unpack, 
print(d) # if we add other, now this have the latest element 


# None 
print(None) # None value