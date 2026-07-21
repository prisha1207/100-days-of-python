#importing random module
import random

# #generating random integers between points a and b where both a and b are included
# random_int=random.randint(1,10)
# print(random_int)
#
# #random.random() vs random.uniform()
# random_type1=random.random() #BETWEEN 0 AND 1 where 0 is included
# print(random_type1)
#
# random_type2=random.uniform(0,1) # includes both a and b but might never show due to round-off bounds
# print(random_type2)

#HEAD OR TAIL
random_head_or_tail=random.randint(0,1)
if random_head_or_tail == 1:
    print("HEADS!")
else:
    print("TAILS!")

