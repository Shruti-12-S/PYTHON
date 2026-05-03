'''Question: Write a program to swap the values of two numbers entered by the user'''

a=int(input("Enter first integer: "))
b=int(input("Enter second integer: "))

temp=a
a=b
b=temp

print("Value of a after swapping: ", a)
print("Value of b after swapping: ", b)