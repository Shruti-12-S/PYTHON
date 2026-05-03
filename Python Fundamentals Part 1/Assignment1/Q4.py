'''Question: The user enters a string containing a number (e.g., "45"). 
Convert it to an integer, a float, and a string again. 
Print all three values with their types.'''

num_str = input("Enter a number as a string: ")
num_int = int(num_str)
num_float = float(num_str)
num_str_again = str(num_int)

print("Integer value:", num_int, "Type:", type(num_int))
print("Float value:", num_float, "Type:", type(num_float))
print("String value:", num_str_again, "Type:", type(num_str_again))