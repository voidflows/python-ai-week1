#Approach 1

number = int(input("Enter any number : "))
fact = 1

for i in range(1,number+1):
    fact*=i
print(fact)

#Approach 2
def calc_fact(n):
    if n == 0:
        return 1
    else:
        return n * calc_fact(n-1)

#result = calc_fact(6)
result = int(input("Enter any number : "))
print(calc_fact(result))