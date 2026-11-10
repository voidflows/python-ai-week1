
import json
from pathlib import Path

# ---------------------------------------
# LOAD STUDENT DATA FROM JSON FILE
# ---------------------------------------

# Get the location of students.json
# in the same directory as main.py
file_path = Path(__file__).resolve().parent / "students.json" #(__file__) = path of current python script and Path(__file__).resolve() = Absolute path of main.py

if file_path.exists():
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            students = json.load(file)
    except (json.JSONDecodeError, OSError) as error:
        print(f"Unable to load student data: {error}")
        raise SystemExit(1)
else:
    students = []


# ---------------------------------------
# STUDENT MANAGEMENT SYSTEM
# ---------------------------------------

while True:

    print("\n============= STUDENT MANAGER =============")
    print("1. Add Student")
    print("2. View Students")
    print("3. Calculate Result")
    print("4. Find Topper")
    print("5. Search Student")
    print("6. Exit")

    choice = input("Enter your choice : ")


    # ---------------------------------------
    # OPTION 1: ADD STUDENT
    # ---------------------------------------

    if choice == "1":

        name = input("Enter name : ").strip()

        if not name:
            print("Student name cannot be empty!")
            continue

        try:
            math = int(input("Math marks : "))
            english = int(input("English marks : "))
            science = int(input("Science marks : "))

        except ValueError:
            print("Invalid marks! Please enter numbers.")
            continue

        # Validate marks
        if not (0 <= math <= 100 and
                0 <= english <= 100 and
                0 <= science <= 100):
            print("Marks must be between 0 and 100!")
            continue

        # Create a new dictionary for each student
        student = {
            "name": name,
            "math": math,
            "english": english,
            "science": science
        }

        # Add the dictionary to the students list
        students.append(student)

        # Save the updated list to the JSON file
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(students, file, indent=4)

        except OSError as error:
            students.pop()
            print(f"Could not save student: {error}")
            continue

        print("Student added successfully!!!")


    # ---------------------------------------
    # OPTION 2: VIEW STUDENTS
    # ---------------------------------------

    elif choice == "2":

        if len(students) == 0:
            print("No Students Found!!!")

        else:
            print("\n========== ALL STUDENTS ==========")

            for student in students:
                print(f"Name : {student['name']}")
                print(f"Math : {student['math']}")
                print(f"English : {student['english']}")
                print(f"Science : {student['science']}")
                print("------------------------------")


    # ---------------------------------------
    # OPTION 3: CALCULATE RESULT
    # ---------------------------------------

    elif choice == "3":

        search_student_with_name = input(
            "Enter student name : "
        ).strip()

        found = False

        for student in students:

            if student["name"].lower() == search_student_with_name.lower():

                found = True

                print("Student Found!")

                total = (
                    student["math"] +
                    student["english"] +
                    student["science"]
                )

                average = total / 3

                # Pass marks = 40 in every subject
                if (student["math"] >= 40 and
                    student["english"] >= 40 and
                    student["science"] >= 40):

                    result = "PASS"

                else:
                    result = "FAIL"

                print(f"Total : {total}")
                print(f"Average : {round(average, 2)}")
                print(f"Result : {result}")

                break

        if not found:
            print("No Student Found!!!")


    # ---------------------------------------
    # OPTION 4: FIND TOPPER
    # ---------------------------------------

    elif choice == "4":

        if len(students) == 0:
            print("No Students Found!")

        else:
            highest_total = -1
            topper = None

            for student in students:

                total = (
                    student["math"] +
                    student["english"] +
                    student["science"]
                )

                if total > highest_total:
                    highest_total = total
                    topper = student["name"]

            print(f"Topper is : {topper}")
            print(f"Highest Total is : {highest_total}")


    # ---------------------------------------
    # OPTION 5: SEARCH STUDENT
    # ---------------------------------------

    elif choice == "5":

        search_name = input(
            "Enter name of the student : "
        ).strip()

        found = False

        for student in students:

            if student["name"].lower() == search_name.lower():

                found = True

                print("\nStudent Found!")
                print(f"Name : {student['name']}")
                print(f"Math : {student['math']}")
                print(f"English : {student['english']}")
                print(f"Science : {student['science']}")

                break

        if not found:
            print("No Students Found!")


    # ---------------------------------------
    # OPTION 6: EXIT
    # ---------------------------------------

    elif choice == "6":

        print("Exiting application...")
        break


    # ---------------------------------------
    # INVALID CHOICE
    # ---------------------------------------

    else:
        print("Invalid Choice! Please try again.")
