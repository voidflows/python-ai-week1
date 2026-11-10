# If we want to store several students, we can use a list of dictionaries:[{},{},....]
# List [] stores all students.
# Dictionary {} stores one student's information.

students = [] # students = [] stores all students, so we want to keep it throughout the program.
while True: #while True — keeps the application running.
    print("\n============= STUDENT MANAGER=============")
    print(f"1.Add Student : ")
    print(f"2.View Students : ")
    print(f"3.Calculate Result : ")
    print(f"4.Find Topper : ")
    print(f"5.Search Student : ")
    print(f"6.Exit : ")

    choice = input("Enter your choice : ")

    if choice == "1":
        name = input("Enter name : ")
        math = int(input("Math marks : "))
        english = int(input("English marks : "))
        science = int(input("Science marks : "))
        student = { #student = {} represents one student, so we want to create a fresh dictionary each time a new student is added.
            "name":name,
            "math":math,
            "english":english,
            "science":science
        }
        students.append(student)
        print(f"Student added successfully!!!")
        print(students)
    elif choice == "2":
        if len(students) == 0:
            print("No Students found!!!")
        else:
            for student in students:
                print(f"Name : {student["name"]}")
                print(f"Math : {student["math"]}")
                print(f"English : {student["english"]}")
                print(f"Science : {student["science"]}")
    elif choice == "3":
        search_student_with_name = input("Enter student name : ").strip()
        found = False
        for student in students:
            if student["name"].lower() == search_student_with_name.lower():
                found = True
                print("Student Found")

                total = student["math"] + student["english"] + student["science"]
                average = total/3

                if(student["math"] >=40 and student["english"] >=40 and student["science"] >=40):
                    result = "PASS"
                else:
                    result = "FAIL"
                print(f"Total : {total}")
                print(f"Average : {round(average,2)}")
                print(f"Result : {result}")
                break
        if not found:
            print("No Student Found!!!")

    elif choice == "4":

        if len(students) == 0:
            print("No Students Found")

        highest_total = -1
        topper = None

        for student in students:
            total = student["math"] + student["english"] + student["science"]

            if(total > highest_total):
                highest_total = total
                topper = student["name"]
        print(f"Topper is : {topper}")
        print(f"Highest Total is  : {highest_total}")
    elif choice =="5":
        search_name = input("Enter name of the student : ").strip()
        found = False

        for student in students:
            if student["name"].lower() == search_name.lower():
                found = True
                print(f"Name : {student["name"]}")
                print(f"Math : {student["math"]}")
                print(f"English : {student["english"]}")
                print(f"Science : {student["science"]}")
                break
        if not found:
            print("No Students are found")
                
    elif choice == "6":
        print(f"Exiting application")
        break # break — exits the application when the user chooses 6.
    else:
        print(f"Invalid Choice")
