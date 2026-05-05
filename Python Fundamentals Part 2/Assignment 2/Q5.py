'''
Write a function to return the sum of the digits of a number, n
'''

def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total

number = int(input("Enter a number: "))
print(f"The sum of the digits in {number} is: {sum_of_digits(number)}")