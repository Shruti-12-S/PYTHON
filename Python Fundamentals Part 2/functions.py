# def hello():
#     print("Hello World")

# hello()
# hello()

# '''Function definition'''
# def sum(a,b): #parameters
#     s=a+b
#     return s

# result = sum(4,3)#arguments
# print(result)
# print(sum(21,54))


'''function to print average of 3 numbers'''
# def calc_avg(a,b,c):
#     sum=a+b+c
#     return sum/3

# print(calc_avg(15,10,45))

'''default value for parameters'''
# def sum(a,b=1):
#     return a+b

# print(sum(4))
# print(sum(4,5))


'''lambda function'''
# sum=lambda a,b:a+b
# print(sum(4,5))

# avg = lambda a,b:(a+b)/2
# print(avg(10,20))

'''WAP to print factorial of n'''
def calc_factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

n=int(input("Enter a number: "))
print(f"Factorial of {n} is {calc_factorial(n)}")