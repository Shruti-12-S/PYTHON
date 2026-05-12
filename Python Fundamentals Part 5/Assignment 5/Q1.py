'''
Create a program that:
1. Opens a file "names.txt" in write mode
2. Writes 5 names (one per line) entered by the user
3. Then opens the same file in read mode and prints all names
'''

with open("C:/Users/Shruti/OneDrive/Desktop/AIML PRIME 2.0/PYTHON/Python Fundamentals Part 5/Assignment 5/names.txt","w") as file:
    print("Enter 5 names: ")

    for i in range(5):
        name = input(f"Enter name {i+1}: ")
        file.write(name + "\n")

with open("C:/Users/Shruti/OneDrive/Desktop/AIML PRIME 2.0/PYTHON/Python Fundamentals Part 5/Assignment 5/names.txt","r") as file:
    print("\nNames stored in the file: ")

    for line in file:
        print(line.strip())
