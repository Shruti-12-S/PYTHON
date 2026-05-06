marks=[99,89,100,65,92,"abc",100.99]
print(marks[4])
print(len(marks))

marks[2]=70
print(marks)
print(type(marks))
print(marks[5:])
print(marks[-5:-2])

'''lists methods'''
nums=[1,2,3]
nums.append(4)
print(nums)

nums.insert(2,10)
print(nums)

nums.reverse()
print(nums)

nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

'''Using loops with lists'''
num=[1,2,3,10,4]
for val in num:
    print(val)

'''find x in list and return its index'''

x=10
idx=0
for val in num:
    if val==x:
        print(f"{x} Found at index {idx}")
        break
    idx+=1


