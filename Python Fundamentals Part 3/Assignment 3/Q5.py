'''
Create a dictionary where:
• Keys=student names
• Values=marks(integer)
Write a menu-based program where user presses a key (ʼAʼ,‘Bʼ,‘Cʼ,‘Dʼ) depending on the operation they want to perform on the dictionary:
1. A - Add a student 
2. B - Update marks 
3. C - Search for a student 
4. D - Display all students and marks
'''

students = {}

while True:
    print("\n----- MENU -----")
    print("A - Add a student")
    print("B - Update marks")
    print("C - Search for a student")
    print("D - Display all students")
    print("E - Exit")

    choice = input("Enter your choice: ").upper()

    match choice:
        case 'A':
            name = input("Enter student name: ")
            marks = int(input("Enter marks: "))
            students[name] = marks
            print("Student added successfully!")

        case 'B':
            name = input("Enter student name to update: ")
            if name in students:
                marks = int(input("Enter new marks: "))
                students[name] = marks
                print("Marks updated successfully!")
            else:
                print("Student not found!")

        case 'C':
            name = input("Enter student name to search: ")
            if name in students:
                print(f"{name}'s marks: {students[name]}")
            else:
                print("Student not found!")

        case 'D':
            if students:
                print("\nStudent Records:")
                for name, marks in students.items():
                    print(name, ":", marks)
            else:
                print("No records found!")

        case 'E':
            print("Exiting program...")
            break

        case _:
            print("Invalid choice! Please try again.")
