'''
Write a function is_prime(n) that returns True if n is a prime number and False otherwise, using a loop.
[Hint - 
1.We only check prime for 2 or numbers greater than 2. 2 is the smallest prime number.
2.A non-Prime number n,will always get divided by atleast one number in range[2,n-1].

Eg- For number 9 weʼll check in range(2,8) & itʼll get divided by 3. So 9 is non-prime & weʼll return False for it.
For number 7 weʼll check in range(2,6) & it wonʼt get divided by any. So 7 is prime & weʼll return True for it.]
'''

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
    