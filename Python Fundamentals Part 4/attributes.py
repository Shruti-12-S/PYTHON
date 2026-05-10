#attributes: class & instance attributes

class Student:
    college_name = "ABC College" #class attribute
    PI = 3.1 #class attribute


    def __init__(self,name,cgpa):#parameterized constructor:
        self.name = name #instance attribute
        self.cgpa = cgpa #instance attribute
        self.PI = 3.14 #instance attribute

stud1 = Student("Rahul", 8.5)

print(stud1.name) #accessing instance attribute
print(stud1.cgpa) #accessing instance attribute 
print(stud1.college_name) #accessing class attribute
print(Student.college_name) #accessing class attribute using class name
#print(Student.name) #error: cannot access instance attribute using class name
print(stud1.PI) #accessing instance attribute
print(Student.PI) #accessing class attribute using class name
