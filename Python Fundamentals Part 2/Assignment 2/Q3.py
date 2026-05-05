'''
Write a function that prints the digits of a number. For example, n=312 if there are 3 digits in it 3, 1, and 2, & we need to print them.
[Hint - The rightmost digit of a number N is N % 10. And to remove the rightmost digit from a number, we can do N = N / 10]
'''

# def print_digits(n):
#     while n > 0:
#         digit = n % 10
#         print(digit)
#         n = n // 10


# number = int(input("Enter a number: "))
# print(f"The digits of the number {number} are:")
# print_digits(number)


n = int(input("Enter a number: "))
digits = []

while n > 0:
    digits.append(n % 10)
    n = n // 10

digits.reverse()

for d in digits:
    print(d)