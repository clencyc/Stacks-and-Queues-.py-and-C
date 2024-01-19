import random
import math

#1. An Outer loop decreases in size each time
#2. The goal is to have the largest number at the end of the
#     list when the outer loop completes 1 cycle
#3. The inner loop starts comparing indexes at the beginning
#    of the loop
#4. Check if list[index] > list [index + 1]
#5. If so swap the indes values
#6. When the inner loop completes the largest number is ar
#   the end of the list
#7. Decreament the outer loop by 1

numbers = []
for i in range (5):
    numbers.append(random.randrange(1,10))
#to get each index number

i = len(numbers) - 1
while i > 1:
    j = 0

    while j < i:
        print("\n Is {} > {}".format(numbers[j],numbers[j+1]))
        if numbers[j] > numbers[j + 1]:

            print(("Switch"))
            #to swap the values
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp
        else:
            print()
            print("Don't switch")

        j+=1

        for k in numbers:
            print(k, end=", ")
        print()
    print("END OF ROUND")

    i -= 1

for k in numlist:
    print(k, end=", ")
print()