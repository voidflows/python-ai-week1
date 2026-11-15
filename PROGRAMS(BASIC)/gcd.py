num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))

# We find the smaller number to decide how far our loop needs to run when calculating HCF/GCD.
if num2>num1:
    smallest = num1
else:
    smallest = num2

hcf = 1
for i in range(1,smallest+1):
    if(num1 % i == 0 and num2%i == 0):
        hcf = i
print(f"HCF is : {hcf}")
