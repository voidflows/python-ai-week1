nums = [1,2,3,4,5,6,7,8,9,10]
even = []
odd = []

for i in nums:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(even)
print(odd)
print(len(even))
print(len(odd))
print(sum(even))
print(sum(odd))