# Strings
print("\nPython - Strings ")
print('Hello') # string
print("Hello") # string
print(type('Hello'))
print(type("Hello"))

username = 'User'
password = '45secret'

# For long strings use '''
long_string = '''
line 1
line 2
------
''' 
print(long_string)

# Some operations with strings
first_name = 'Name'
last_name = 'Lastname'
full_name = first_name + ' ' + last_name
print(full_name)


# String concatenation and convert (cast) number to string 
print("\nPython - Concatenation an Type conversion ")
print('hello' + 'world')
print('hello ' + str(100))

# Type Conversion
print(type(str(100)))
print(type(int(str(100))))
a = str(100)
b = int(a)
c = type(b)
print(c)


# Escape Sequences
print("\nPython - Escape Sequences ")
weather = "It's sunny" # with ""
print(weather)
weather = 'It\'s sunny' # with escape sequence \
print(weather)
weather = "It\'s \"kind of\" sunny" # with escape sequence \
print(weather)
weather = "\t It\'s \"kind of\" sunny" # add tab '\t'
print(weather)
weather = "It\'s \"kind of\" sunny \nhope you have a good day!" # add newline '\n'
print(weather)



# Formatted Strings
print("\nPython - Python 3 & 2 Formatted Strings ")
name = 'John'
age = 55
print('Hi ' + name + '. You are ' + str(age) + ' years old')
# python 3 Formatted Strings (More easy way) 
print(f'Hi {name}. You are {age} years old')


# Python2 Formatted Strings
print('Hi {}. Your are {} years old.'.format(name, age))
print('Hi {}. Your are {} years old.'.format(name, age))
print('Hi {1}. You are {0} years olf.'.format(age, name))
print('Hi {new_name}. You are {age} years old.'.format(new_name='Sally', age=100))



# String Indexes
# String Slicing
# [Start : Stop : Step-over]
print("\nPython - String Indexes, Slicing ")
selfish = '01234567'

print(selfish[0]) # index 0
print(selfish[7]) # index 7
print(selfish[0:2]) # from index 0 to index 2
print(selfish[0:8]) # from index 0 to index 8 (all string)
print(selfish[0:8:2]) # from index 0 to index 8 with steps of 2

print(selfish[1:])  # from index 0 to whatever is the end
print(selfish[:5])  # whatever at beggining to index 5
print(selfish[::1]) # all with steps 1 

print(selfish[-4]) # negative index means to start at end
print(selfish[::-1]) # to get the reverse of the string 
print(selfish[::-2]) # to get the reverse with 2 steps

# Immutability - Strings in python are immutable ( they cannot be change once created) 
# to modify we need to create a new string
# Example:
# selfish[2] = '0' # Error cannot change character once string selfish is already created


# Built-in Functions and Methods
print("\nPython - Built-in Functions and Methods ")
print(len('Helllooooo')) # lenght of string

quote = 'to be or not to be'
print(quote.upper())        # capitalize all string
print(quote.capitalize())   # capitalize just begging of string
print(quote.find('be'))     # find index of first ocurrence of 'be' 
print(quote.replace('be', 'me')) # replace all occurrences of 'be' with 'me'
print(quote) # important: because strings are immutable replace create a new string
# example
quote2 = quote.replace('be', 'me')
print(quote2) 