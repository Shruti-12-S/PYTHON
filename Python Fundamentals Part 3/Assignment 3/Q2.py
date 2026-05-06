'''
Given a list of integers, compute the average of all numbers in the list
'''

list = [1,2,3,4,5]

sum=0
n=len(list)
for num in list:
    sum+=num

print(f"average is : {sum/n}")
