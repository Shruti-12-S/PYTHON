'''
Create a program that:
1. Opens a file "log.txt" in append mode
2. Adds a new log entry (like "Program run successfully")
3. Opens the file in read mode and prints all logs
'''

with open("C:/Users/Shruti/OneDrive/Desktop/AIML PRIME 2.0/PYTHON/Python Fundamentals Part 5/Assignment 5/log.txt","a") as file:
    file.write("Program run successfully\n")

with open("C:/Users/Shruti/OneDrive/Desktop/AIML PRIME 2.0/PYTHON/Python Fundamentals Part 5/Assignment 5/log.txt","r") as file:
    print("All Logs:\n")

    for line in file:
        print(line.strip())