'''
Create a program that: 
1. Has a list of numbers: [5, 10, 15, 20, 25]
2. Uses a list comprehension to create a new list with only numbers greater than 15
3. Prints the new list
'''

list = [5,10,12,20,25]
newList = [nums for nums in list if nums>15]

print(newList)