class Student:

    def __init__(self):#default constructor
        print("obj is being constructed..")

    def __init__(self,name,cgpa):#parameterized constructor
        self.name = name
        self.cgpa = cgpa

    def get_cgpa(self):
        return self.cgpa

stud1 = Student("Rahul", 8.5)
stud2 = Student("Priya", 9.0)
stud3 = Student("Rutik", 7.5)

print(stud1.name)
print(stud2.name)
print(stud3.name)

print(f"{stud1.name} has a CGPA of {stud1.get_cgpa()}")
print(f"{stud2.name} has a CGPA of {stud2.get_cgpa()}")
print(f"{stud3.name} has a CGPA of {stud3.get_cgpa()}")

'''Types of constructors'''
