'''
Ask the user for a string and print:
• All unique characters
• The count of unique characters
'''

string = input("Enter a string: ")
unique_characters = set(string)
print(f"Unique characters: {unique_characters}")    
print(f"Count of unique characters: {len(unique_characters)}")