'''Question:Ask the user for a temperature in Celsius (string input). Convert it to float, then calculate and print the temperature in Fahrenheit 
Conversion formula:FahrenheitTemp=(CelsiusTemp∗(9/5))+32
'''

temp_celcius=input("Enter temperature in celcius: ")
temp_float=float(temp_celcius)

fahrenheit=(temp_float*(9/5))+32
print("Temperature in Fahrenheit: ", fahrenheit)