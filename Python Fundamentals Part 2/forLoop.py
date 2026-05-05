string = "hello"

if "o" in string:
    print("o is present in the string")

# in is membership operator, it checks if the value is present in the sequence or not
for var in string:
    print(var)


for i in range(5):
    print("hello")


word="artificial intelligence"
#count the number of i's => 5
ans=0
for ch in word:
    if ch == "i":
        ans+=1

print(ans)


'''print vowel count of a given string'''
word="artificial"
count =0
for ch in word:
    if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
        count+=1
print(count)


'''range function'''
for i in range(2,11,2):
    print(i)


'''print sum of first n natural numbers'''
n = int(input("Enter a number: "))
sum=0
for i in range(1,n+1):
    sum+=i
print(" Sum is", sum)