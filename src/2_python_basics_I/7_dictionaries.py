# Dictionaries, : other languages also called hash table or map,
# data structure with unorder key-value pairs 
# lists are order data structure, dictionary store more information
# keys needs to be unmuable (cannot change), if there are same keys last value is taken (overwrite value)  

print("\nPython - Dictionaries ")
dictionary = {
    'a': [1, 2, 3],
    'b': 'Hello',
    'c': True
}

print(dictionary['a'][1]) # find 'a' key, index 1 or list
print(dictionary) # print all dictionary


# Dictionary Methods
print('\nDictionary Methods')
user = {
    'basket': [1, 2, 3],
    'greet': 'Hello',
    'age': 20
}

print(user.get('age', 55))  # to find if key='age' exists, if not use default value=55

user2 = dict(name='JohnJohn') # other way to create a dictionary, built-in function dict(key=value)
print(user2)

print('basket' in user) # other to look for a value in a dictionary
print('size' in user)
print('age' in user.keys()) # look in keys
print('Hello' in user.values()) # look in values
print(user.items()) # print all items of dictionary

user2 = user.copy() # copy dictionary
user.clear() # clean
print(user)
print(user2)
print(user2.pop('age')) # removes key 'age', return value
print(user2.popitem())  # removes randomly something
user2.update({'age': 55}) # updates a item
print(user2)