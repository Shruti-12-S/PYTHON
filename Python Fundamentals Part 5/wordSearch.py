'''
print if word "Python" exists. if yes then print line number.
'''

data = True
line = 1
word = "solved"

with open("C:/Users/Shruti/OneDrive/Desktop/AIML PRIME 2.0/PYTHON/Python Fundamentals Part 5/sample.txt","r") as f:
    while data:
        data = f.readline()
        if (word in data):
            print(f"{word} found at line {line}")
            break
        print(data)
        line+=1