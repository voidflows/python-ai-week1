# 1. Write a program to store seven fruits in a list entered by the user.
fruits = []

f1 = input("Enter fruit 1 : ")
fruits.append(f1)

f2 = input("Enter fruit 2 : ")
fruits.append(f2)

f3 = input("Enter fruit 3 : ")
fruits.append(f3)

f4 = input("Enter fruit 4 : ")
fruits.append(f4)

f5 = input("Enter fruit 5 : ")
fruits.append(f5)

f6 = input("Enter fruit 6 : ")
fruits.append(f6)

f7 = input("Enter fruit 7 : ")
fruits.append(f7)

print(fruits)


# 2. Write a program to accept marks of 6 students and display them in a sorted manner(descending order)
marks =[]

m1 = int(input("Enter marks 1 : "))
marks.append(m1)

m2 = int(input("Enter marks 2 : "))
marks.append(m2)

m3 = int(input("Enter marks 3 : "))
marks.append(m3)

m4 = int(input("Enter marks 4 : "))
marks.append(m4)

m5 = int(input("Enter marks 5 : "))
marks.append(m5)

m6 = int(input("Enter marks 6 : "))
marks.append(m6)

marks.sort(reverse=True)
print(marks)

# 3. Check that a tuple type cannot be changed in python.

tup = (1,2,3)
tup[1] = 5
print(tup)

#4. Write a program to sum a list with 4 numbers
number = [1,2,3,4]
print(sum(number))

# 5. Write a program to count the number of zeros in the following tuple:
a = (7, 0, 8, 0, 0, 9)
print(a.count(0))
