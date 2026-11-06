# 1. Write a program to find the greatest of four numbers entered by the user.

n1 = int(input("Enter num 1 : "))
n2 = int(input("Enter num 1 : "))
n3 = int(input("Enter num 1 : "))
n4 = int(input("Enter num 1 : "))

if(n1 > n2 and n1 > n3 and n1 > n4):
    print(f"Largest is {n1}")
elif(n2 > n1 and n2 > n3 and n2 > n4):
    print(f"Largest is {n2}")
elif(n3>n1 and n3 > n2 and n3 >n4):
    print(f"Largest number is {n3}")
else:
    print(f"Largest number is {n4}")

# 2. Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

marks1 = int(input("Enter marks 1 : "))
marks2 = int(input("Enter marks 2 : "))
marks3 = int(input("Enter marks 3 : "))

total = (marks1 + marks2 + marks3)
total_percentage = (100 * total) / 300

if(total_percentage >= 40 and marks1 > 33 and marks2 > 33 and marks3 >33):
    print(f"Passed with {total_percentage}%")
else:
    print(f"Failed with {total_percentage}%")

# 3. A spam comment is defined as a text containing following keywords: “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter message : ")

if(p1 in message or p2 in message or p3 in message or p4 in message):
    print("SPAM MESSAGES")
else:
    print(f"{message}")

# 4. Write a program to find whether a given username contains less than 10 characters or not.

user_name = input("Enter User Name : ")
if(len(user_name)  < 10):
    print(f"Username should contain atleast 10 characters")
else:
    print(f"{user_name}")

# 5. Write a program which finds out whether a given name is present in a list or not.

names = ["Rahul","Trisha","Debanjana","Mousumi","Alok"]
your_name = input("Enter your name : ")
if(your_name in names):
    print(f"{your_name} is present")
else:
    print(f"{your_name} is not found")

# 6. Write a program to calculate the grade of a student from his marks from the following
# scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 => C
# 50 – 60 => D
# <50 => F

marks = int(input("Enter your marks : "))

if(marks <=100 and marks >=90):
    print("Ex")
elif(marks <=90 and marks >=80):
    print("A")
elif(marks <=80 and marks >= 70):
    print("B")
elif(marks <=70 and marks >= 60):
    print("C")
elif(marks < 50):
    print("F")

# 7. Write a program to find out whether a given post is talking about “Harry” or not.

post = input("Enter your post : ")
if("harry".lower() in post.lower()):
    print("The post is talking about you")
else:
    print("The post is not talking about you")