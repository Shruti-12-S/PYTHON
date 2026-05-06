'''
Ask the user for a string and check whether it is a palindrome or not. 
A Palindrome is a string which is same when we read it forward & backward. 
Eg-“madam”,“racecar” etc.

[Hint - A palindrome string is equal to the reversed version of the string. We can use a loop to reverse the string manually.]
'''

string = input("Enter a string: ")
new_string = string[::-1]

if(string == new_string):
    print("The string is a palindrome.")
else:   
    print("The string is not a palindrome.")
