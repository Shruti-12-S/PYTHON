squares = []

for i in range(6):
    squares.append(i*i)

print(squares)


sq = [i*i for i in range(6) if i%2!=0 ]
print(sq)

nums=[-2,-4,3,5,2,-1]

nums=[0 if i<0 else i for i in nums]

print(nums)

words = ["hello", "python", "apnacollege"]
words = [i.upper() for i in words]

print(words)