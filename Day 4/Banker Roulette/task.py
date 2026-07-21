import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# #option-1
# rand_person=random.randint(0,4) #using this to generate a random but valid index
# print(f"{friends[rand_person]} pays the bill!")

#option-2
print(random.choice(friends))

#opt 2 cuz its shorter to code and easier to understand and read