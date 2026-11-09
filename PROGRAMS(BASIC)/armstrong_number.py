num = int(input("Enter any number : "))
temp = num
sum = 0

while temp!=0:
    remainder = temp % 10
    sum+=remainder**3
    temp//=10

if(sum == num):
    print("Armstrong number")
else:
    print("Not an Armstrong number")