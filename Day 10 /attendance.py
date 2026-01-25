print("Student Attendance Checker")
print("---------------------------")

present_count = 0
total_students = int(input("How many students: "))

for i in range(1, total_students + 1):
    name = input(f"Enter student {i} name: ").strip()
    status = input("Present or Absent (p/a): ").lower().strip()

    if status == "p":
        print(f"{name} is Present")
        present_count += 1
    elif status == "a":
        print(f"{name} is Absent")
    else:
        print("Invalid input, marked as Absent")

print("---------------------------")
print("Attendance Summary")
print(f"Total Students: {total_students}")
print(f"Present Students: {present_count}")
print(f"Absent Students: {total_students - present_count}")
