'''
Design a program to continuously input a number from user & print if it is positive or negative until the user enters “Quit”
'''

while True:
    user_input = input("Enter a number (or 'Quit' to exit): ")
    
    if user_input.lower() == "quit":
        print("Exiting the program. Goodbye!")
        break
    
    try:
        number = float(user_input)
        if number > 0:
            print(f"{number} is positive.")
        elif number < 0:
            print(f"{number} is negative.")
        else:
            print("The number is zero.")
    except ValueError:
        print("Invalid input. Please enter a valid number or 'Quit' to exit.")


    