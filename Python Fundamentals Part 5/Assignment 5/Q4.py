'''
Create a Python dictionary of 3 cities and their populations. Save it to "cities.json".
1. Then load the JSON and print each city and its population.
2. Ask the user for a new city & its population-update this info in the json file.
'''

import json

# Try to read existing JSON file
try:
    with open("C:/Users/Shruti/OneDrive/Desktop/AIML PRIME 2.0/PYTHON/Python Fundamentals Part 5/Assignment 5/cities.json", "r") as file:
        data = json.load(file)

except FileNotFoundError:
    # Create initial data if file does not exist
    data = {
        "Mumbai": 20400000,
        "Delhi": 19000000,
        "Bangalore": 13000000
    }

# Print cities and populations
print("Cities and their Populations:\n")

for city, population in data.items():
    print(city, ":", population)

# Ask user for new city and population
new_city = input("\nEnter new city name: ")
new_population = int(input("Enter population: "))

# Update dictionary
data[new_city] = new_population

# Save updated data back to JSON file
with open("C:/Users/Shruti/OneDrive/Desktop/AIML PRIME 2.0/PYTHON/Python Fundamentals Part 5/Assignment 5/cities.json", "w") as file:
    json.dump(data, file, indent=4)

print("\nCity added successfully!")


