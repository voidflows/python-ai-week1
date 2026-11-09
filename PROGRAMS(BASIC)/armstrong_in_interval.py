lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))

for num in range(lower, upper + 1):
    order = len(str(num))
    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** order
        temp //= 10

    if total == num:
        print(num)