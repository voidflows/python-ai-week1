#Approach 1

# Syntax = lambda arguments: expression

n = int(input("Enter any number : "))

power = lambda x : 2**x

for i in range(n):
    print(f" 2 raised power of {i} is {power(i)}")

#Approach 2

power = list(map(lambda x : 2**x,range(n)))
print(power)

