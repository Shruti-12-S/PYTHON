'''Question: Evaluate and print the result of the following expression:
x =10+3*2**2
Based on what you learnt in the lecture, explain why the output is what it is'''
x =10+3*2**2
print(x)

#The output is 22 because of the order of operations in Python. 
# The exponentiation operator (**) has the highest precedence, so 2**2 is evaluated first,
# resulting in 4. Then, the multiplication operator (*) is evaluated next, so 3*4 is calculated,
# giving 12. Finally, the addition operator (+) is evaluated last, so 10+12 is computed, resulting in 22.