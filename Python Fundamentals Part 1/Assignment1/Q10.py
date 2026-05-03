'''Question: Take a decimal number as input (like 45.78) and output its integer part 45 and fractional part .78'''

a=float(input("Enter decimal number: "))

int_part = int(a)
frac_part = a - int_part
print("Integer part is: ", int_part)
print("Fractional part is: ", format(frac_part, ".2f"))
