#infinite loop
# while True:
#     print("Shruti Shinde")


#finite loop => 10x
# count =1 #iterator variable
# while count <= 10:
#     print("Hello World", count)
#     count+=1


# print("After loop", count)


'''Print number from 1 to 5'''
# i=1
# while i<=5:
#     print(i)
#     i+=1


'''print in reverse order from 5 to 1'''
# count =5
# while count>=1:
#     print(count)
#     count-=1    

# i=0
# while i<5:
#     print(i)
#     i+=1


'''Print multiplication table of any number n '''
# n = int(input("Enter a number: "))
# i=0
# while i<10:
#     print(n*(i+1))
#     i+=1


'''break statement => to break the loop when a condition is met'''
# i=1
# while i<=10:
#     if(i%6==0):
#         break
#     print(i)
#     i+=1


'''continue statement => to skip the current iteration when a condition is met'''
# i=1
# while i<=10:
#     if(i%3==0):
#         i+=1
#         continue
#     print(i)
#     i+=1

# print("outside loop")


'''Odd numbers'''
# i=1
# while i<=10:
#     print(i)
#     i+=2

'''odd numbers using continue statement'''
i=0
while i<10:
    i+=1
    if(i%2==0):
        continue
    print(i)


