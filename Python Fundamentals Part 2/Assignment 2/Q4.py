'''
Write a function to return the count the number of digits in a number, n 
'''

def count_digits(n):
    count = 0
    while n > 0:
        count += 1
        n = n // 10
    return count

number = int(input("Enter a number: "))
print(f"The number of digits in {number} is: {count_digits(number)}")