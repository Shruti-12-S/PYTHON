'''
Given a tuple of integers, create: 
• A tuple of all even numbers 
• A tuple of all odd numbers
'''

tuple = (1,2,3,4,5,6,7,8,9,10)
even_tuple = ()
odd_tuple = ()
for num in tuple:
    if(num%2==0):
        even_tuple += (num,)
    else:
        odd_tuple += (num,)

print("Even numbers tuple:", even_tuple)
print("Odd numbers tuple:", odd_tuple)

