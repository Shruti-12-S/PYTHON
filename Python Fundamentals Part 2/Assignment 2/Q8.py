'''
Letʼs create a simple calculator that performs arithmetic operations.
Create a function calculator(a, b, operation) that performs addition, subtraction, multiplication, or division based on the operation parameter.
[operation parameter can have values '+', '-', '*', '/']
'''

def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operation."
    
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
op = input("Enter the operation (+, -, *, /): ")
result = calculator(num1, num2, op)
print(f"The result of {num1} {op} {num2} is: {result}")