# Student Result Management System

students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    
    # Marks input
    try:
        math = float(input("Enter Math marks: "))
        physics = float(input("Enter Physics marks: "))
        chemistry = float(input("Enter Chemistry marks: "))
    except ValueError:
        print("Please enter valid numbers for marks!")
        return

    total = math + physics + chemistry
    percentage = total / 3

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B+"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "F"

    student = {
        "Name": name,
        "Roll": roll,
        "Math": math,
        "Physics": physics,
        "Chemistry": chemistry,
        "Total": total,
        "Percentage": round(percentage, 2),
        "Grade": grade
    }

    students.append(student)
    print(f"Student {name} added successfully!\n")

def view_students():
    if not students:
        print("No students added yet.\n")
        return

    print("\n------ All Students ------")
    for s in students:
        print(f"Name: {s['Name']}, Roll: {s['Roll']}, Total: {s['Total']}, "
              f"Percentage: {s['Percentage']}%, Grade: {s['Grade']}")
    print("---------------------------\n")

def main():
    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()
