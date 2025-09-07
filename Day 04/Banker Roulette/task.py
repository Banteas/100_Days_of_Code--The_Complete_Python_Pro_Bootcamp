import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Option 1

# random_friend = random.choice(friends)
# print(random_friend)

print(random.choice(friends))

# Option 2

random_index = random.randint(0,4)

print(friends[random_index])