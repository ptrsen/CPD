#fix this code so that it prints a sorted list of all of our friends (alphabetical). 
friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

new_friend = ['Stanley']

# Answer
friends.extend(new_friend)
print(sorted(friends))
