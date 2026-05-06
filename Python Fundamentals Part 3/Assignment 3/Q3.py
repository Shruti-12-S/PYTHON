'''
Input two lists of integers from the user. Merge them into one list and sort the result.
Eg- list1 = [1, 2, 7] list2 = [2, 4, 5]
result = [1, 2, 3, 54, 5, 7]
'''

list1 = list(map(int, input("Enter the first list of integers (comma separated): ").split(',')))
list2 = list(map(int, input("Enter the second list of integers (comma separated): ").split(',')))

merged_list = list1 + list2
merged_list.sort()
print(merged_list)