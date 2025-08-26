import random

#print(random.randint(1,10))

random_number_0_to_1 = random.random()
print(round(random_number_0_to_1, 2))

random_float = round(random.uniform(1,10),2)
print(random_float)

coin_drop = random.randint(0,1)
if coin_drop == 0:
    print("heads")
else:
    print("tails")