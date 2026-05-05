username=input("Enter username:")
password=input("Enter password:")

if(username=="admin" and password=="pass"):
    print("Login successful!")
else:
    if (username!="admin" and password!="pass"):
        print("Invalid username and password!")
    elif(password!="pass"):
        print("Invalid password!")
    else:
        print("Invalid username!")