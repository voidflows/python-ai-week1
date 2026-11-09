num = int(input("Enter a number : "))
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2,num):
        if(num%i == 0):
            is_prime = False
            break
if is_prime:
    print(f"{num} is Prime")
else:
    print(f"{num} is not Prime")