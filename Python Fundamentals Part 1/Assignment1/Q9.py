'''Question: Ask the user for: Principal(P),Rate(R),Time(T). Convert all to float and calculate Simple Interest
SI=(P*R*T)/100'''

P=float(input("Enter value of P: "))
R=float(input("Enter value of R: "))
T=float(input("Enter value of T: "))

SI=(P*R*T)/100
print("Simple Interest is: ", SI)