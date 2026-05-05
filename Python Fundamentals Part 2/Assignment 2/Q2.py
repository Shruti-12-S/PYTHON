'''
Write a function that takes two integers and prints all even numbers between them (inclusive)
'''

def print_even_numbers(a, b):
    for num in range(a, b + 1):
        if num % 2 == 0:
            print(num)

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
print(f"Even numbers between {num1} and {num2} are:")
print_even_numbers(num1, num2)