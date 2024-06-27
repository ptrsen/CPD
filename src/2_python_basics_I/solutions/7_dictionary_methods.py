# Exercise Dictionary Methods

# 1 Create a user profile for your new game.
# This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'

user_profile = {
    'age' : 10, 
    'username' : 'user', 
    'weapons' : [], 
    'is_active' : True,
    'clan' : 'clan1'
}

# 2 iterate and print all the keys in the above user.
print(user_profile.keys())

# 3 Add a new weapon to your user
user_profile['weapons'].extend(['weapon 1'])
print(user_profile.items())

# 4 Add a new key to include 'is_banned'. Set it to false
user_profile.update({'is_banned': False})
print(user_profile.items())

# 5 Ban the user by setting the previous key to True
user_profile['is_banned'] = True
print(user_profile.items())

# 6 create a new user2 my copying the previous user and update the age value and username value.
user2_profile = user_profile.copy()
user2_profile.update({'age': 50, 'username': 'User2'})
print(user2_profile.items())