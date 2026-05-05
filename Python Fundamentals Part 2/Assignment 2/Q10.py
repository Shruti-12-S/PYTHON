'''
Letʼs create a "Number Guessing Game". Given a secret number (already decided by you), write a program that asks the user to guess it and prints:
- "Too high" if the guess is above the number
- "Too low" if the guess is below the number
- "Correct!" if the guess matches the number
'''

secret_number = 42  # You can change this to any number you like    
while True:
    try:
        guess = int(input("Guess the secret number: "))
        
        if guess > secret_number:
            print("Too high")
        elif guess < secret_number:
            print("Too low")
        else:
            print("Correct!")
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")