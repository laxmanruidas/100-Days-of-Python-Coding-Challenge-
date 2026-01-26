# Day 11 - Student Result Manager
# 100 Days of Python Challenge

students = []

def show_menu():
    print("*" *25)
    print("\nStudent Result Manager")
    print("*" *25)
    print("1. Add Student Result")
    print("2. View All Results")
    print("3. Exit")

def calculate_grade(avg):
    if avg >= 80:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "Fail"

while True:
    show_menu()
    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        name = input("Enter student name: ").strip()
        roll = input("Enter roll number: ").strip()

        sub1 = int(input("Enter marks for Subject 1: "))
        sub2 = int(input("Enter marks for Subject 2: "))
        sub3 = int(input("Enter marks for Subject 3: "))

        total = sub1 + sub2 + sub3
        average = total / 3
        grade = calculate_grade(average)

        student = {
            "name": name,
            "roll": roll,
            "total": total,
            "average": average,
            "grade": grade
        }

        students.append(student)
        print("Student result added successfully.")

    elif choice == "2":
        if not students:
            print("No student records found.")
        else:
            print("\nAll Student Results")
            print("-"*27)
            for student in students:
                print(f"Name: {student['name']}")
                print(f"Roll: {student['roll']}")
                print(f"Total: {student['total']}")
                print(f"Average: {student['average']}")
                print(f"Grade: {student['grade']}")
                print("--"*20)

    elif choice == "3":
        print("Program End. Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")
