# #TOPIC - STRINGS(sequence of characters,index starts with zero)

topic = "knowledge"
print(len(topic))
print(topic[0:4]) #slice
print(topic.upper())

#Using f string
name = "Rahul"
Salary = 50000
print(f"Hi {name},Your salary will be Rs{Salary}")

age = int(input("Enter your age")) #By default input() returns a string.We need to type cast it if we want any other data type
print(age)
print(type(age))

num = int(input("Enter any number : "))
try: #Testing try-except
    print(num/0)
except ZeroDivisionError:
    print("Invalid input")

test = "   Knwoledge engineering   "
print(len(test.strip().title())) #strip() = for removing white spaces,len = calculate total no.of letters and title makes the letter of the first word in capital

age_calculate = int(input("Enter your age : "))
try:
    if(age_calculate < 0):
        print("Age can not be negative")
    else:
        print(f"After 5 years {age_calculate+5}")
except ValueError:
    print("Invalid Whole Number")

marks = 55
passing_marks = 40

if(marks <= passing_marks): #if-else,if-elif-else
    print("Fail")
else:
    print("Pass")

thickness = 7.0
if thickness < 5.0 :
    print("Too Low")
elif thickness > 10.0:
    print("Too High")
else:
    print("Acceptable")


