# 1. Write a program to print multiplication table of a given number using for loop.
number = int(input("Enter any number : "))
for i in range(1,11):
    print(f"{number} * {i} = {number * i}")

# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
l = ["Harry", "Soham", "Sachin", "Rahul"]

for items in l:
    if(items.startswith("S")):
        print(f"Greetings,{items}")
    else:
        print("None of the names starts with S")

# 3. Attempt problem 1 using while loop
num = int(input("Enter any number : "))
i=1
while(i < 11):
    print(f"{num} * {i} = {num * i}")
    i+=1

# 4. Write a program to find whether a given number is prime or not.
n = int(input("Enter any  number : "))
is_prime = True

if(n<=1):
    is_prime = False
else:
    for i in range(2,n):
        if(n%i == 0):
            is_prime = False
            break
if is_prime:
    print(f"{n} is Prime")
else:
    print(f"{n} is not prime")

# 5. Write a program to find the sum of first n natural numbers using while loop
nu = int(input("Enter any natural number : "))
sum = 0
i = 1
while(i <= nu):
    sum+=i
    i+=1
print(sum)

#Using for loop
# user_input = int(input("Enter range : "))
# sum = 0
# for i in range(1,user_input+1):
#     sum+=i
# print(sum)

# 6. Write a program to calculate the factorial of a given number using for loop.
nums = int(input("Enter any number : "))
fact = 1

if(nums < 0):
    print("Factorial for negative number is not possible")

for i in range(1,nums+1):  #while(i <= n) and also take i=1 when using while loop
    fact*=i
    i+=1
print(fact)

# 7. Write a program to print the following star pattern.
# *
# ***
# ***** for n = 3

rows = int(input("Enter no.of rows : "))
for i in range(1,rows+1):
    print("*" * (2*i-1))

# 10. Write a program to print multiplication table of n using for loops in reversed order.

rev = int(input("Enter number : "))
for i in range(10,0,-1): # start with 10,stop before reaching zero,decrease by 1 each time 
    print(f"{rev} * {i} = {rev * i}")

#range(1, 11)       # 1, 2, 3, ... 10
# range(10, 0, -1)   # 10, 9, 8, ... 1
# range(11, 1)       # Empty range
# range(11, 1, -1)   # 11, 10, 9, ... 2

#Remeber range always increases by 1


