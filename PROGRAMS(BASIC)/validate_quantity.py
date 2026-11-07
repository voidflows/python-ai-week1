quantity = int(input("Enter quantity : "))
try:
    if(quantity >= 0):
        print("Accepted")
    else:
        print("Invalid")
except ValueError:
    print("Invalid")