#generate a random list of a random list with 5 values btwn 1 and 9
import random
import math

numbers = []
for i in range (5):
    numbers.append(random.randrange(1,10))

for i in numbers:
    print(i)

