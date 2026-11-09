year = int(input("Enter year : "))

if(year%400 == 0 or (year%4==0 and year%100!=0)):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap year")

# A year divisible by 400 is a leap year.
#A year is also a leap year when it is divisible by 4 but not by 100.