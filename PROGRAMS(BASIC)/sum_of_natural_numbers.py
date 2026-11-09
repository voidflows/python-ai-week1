#Approach 1

n = int(input("Enter any  number : "))
total = 0

for i in range(1,n+1):
    total+=i

print(total)

#Approach 2
i = 1
while i<=n:
    total+=i
    i+=1

print(total)

#Approach 3

total = (n*(n+1)) // 2
print(total)