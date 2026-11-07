#Suqare root = number ** (1/2) or number ** 0.5
import math

#With only one number
# number = float(input("Enter a number : "))
# sq_root = math.sqrt(number)
# print(sq_root)

#With all numbers present in list
numbers = [25,36,49,64]
for i in numbers:
    sq_root = math.sqrt(i)
    print(sq_root)