import random
import math

randlist = ["string", 1,234, 28]
oneToTen = list(range(10))

randlist = randlist + oneToTen
print(randlist[0])
print("List length : ", len(randlist))
first3 = randlist[0:3]

for i in first3:
    print("{} : {}".format(first3.index(i), i))

print(first3[0] * 3)
print("string" in first3)
print("Index of string :", first3.index("string"))

print("How many strings :", first3.count("string"))

first3[0] = "New string"
first3.append("another")

for i in first3:
    print("{} : {}".format(first3.index(i), i))
