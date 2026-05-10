'''
Concept: Encapsulation
Create a class Student with private attributes_name,_roll_no, and _marks.
Provide getter and setter methods with validation (e.g., marks cannot be negative,
roll number has to be between 1 & 100 & name cannot be empty)
'''

class Student:
    def __init__(self,name,roll_no,marks):
        self.set_name(name)
        self.set_roll_no(roll_no)
        self.set_marks(marks)

    # Setter for name
    def set_name(self, name):
        if name.strip() == "":
            print("Name cannot be empty.")
        else:
            self._name = name

    # Getter for name
    def get_name(self):
        return self._name
    
    # Setter for roll number
    def set_roll_no(self, roll_no):
        if 1 <= roll_no <= 100:
            self._roll_no = roll_no
        else:
            print("Roll number must be between 1 and 100.")

        
    # Getter for roll number
    def get_roll_no(self):
        return self._roll_no

    # Setter for marks
    def set_marks(self, marks):
        if marks >= 0:
            self._marks = marks
        else:
            print("Marks cannot be negative.")

    # Getter for marks
    def get_marks(self):
        return self._marks

    # Display student details
    def display(self):
        print("Student Name :", self._name)
        print("Roll Number  :", self._roll_no)
        print("Marks        :", self._marks)


# Creating object
s1 = Student("Rahul", 25, 88)

# Display details
s1.display()

# Updating values using setters
s1.set_marks(95)
s1.set_roll_no(50)
s1.set_name("Aman")

print("\nUpdated Details:")
s1.display()