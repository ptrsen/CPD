# Exercise Password Checker
# Write a program which tells the lenght of the password of a user
# it receives the username and password

username = input('Enter your username:\t')
password = input('Enter you password:\t')

secret_password = len(password) * '*'
print(f'Hey {username}, your password {secret_password} is {len(password)}  letters long.')