# Loop = Repeat the operation which following a rule.

#e.g.1
for i in range(1,6):
    print(i)

#e.g.2
sum = 0
for i in range(1,6):
    sum+=i
print(sum)

#e.g.3
count = 1
while(count <= 3):
    print(count) #if i finish the line here then there will be an infinite loop which will be printing 1 until stackoverflow error comes
    count+=1