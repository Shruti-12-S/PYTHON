# f = open("C:/Users/Shruti/OneDrive/Desktop/AIML PRIME 2.0/PYTHON/Python Fundamentals Part 5/sample.txt") #reading [default]
# print(f.read())

# f = open("C:/Users/Shruti/OneDrive/Desktop/AIML PRIME 2.0/PYTHON/Python Fundamentals Part 5/sample.txt","a") #writing, appends at end
# f.write("\nNew text being appended\n to the file")

# f = open("C:/Users/Shruti/OneDrive/Desktop/AIML PRIME 2.0/PYTHON/Python Fundamentals Part 5/sample2.txt","x") #creates new and open for writing
# f.write("Some random text")

# f = open("C:/Users/Shruti/OneDrive/Desktop/AIML PRIME 2.0/PYTHON/Python Fundamentals Part 5/sample.txt","r+") 
# f.write("123")
# print(f.read())

# f = open("C:/Users/Shruti/OneDrive/Desktop/AIML PRIME 2.0/PYTHON/Python Fundamentals Part 5/sample.txt","a+") 
# f.write("123")
# print(f.read())

f = open("C:/Users/Shruti/OneDrive/Desktop/AIML PRIME 2.0/PYTHON/Python Fundamentals Part 5/sample.txt","w+") 
f.write("123")
print(f.read())



f.close()