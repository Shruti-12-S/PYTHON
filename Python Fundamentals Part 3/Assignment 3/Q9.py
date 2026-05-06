'''
Given a list, print all elements that appear more than once in the list. 
[Hint - use sets]
'''

list = [1,2,3,4,5,2,3,6]
seen = set()
duplicates = set()
for num in list:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print("Elements that appear more than once:", duplicates)