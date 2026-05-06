tup = (1,2,3,4,5,"abc",3.14)
print(tup)
print(type(tup))
print(len(tup))
print(tup[2])

# tup[2]=10  # This will raise an error because tuples are immutable

tup1=(1)
tup2=("abc")
print(type(tup1))  # This will print <class 'int'>, not a tuple
print(type(tup2))  # This will print <class 'str'>, not a tuple

tup3=(1,)  # This is a tuple with one element
print(type(tup3))  # This will print <class 'tuple'>

'''Slicing in tuples'''
print(tup[0:3])

'''loops in tuples'''
tup4 = (1,2,3,4,5)
sum=0
for val in tup4:
    sum+=val
print(f"Sum of elements in tup4: {sum}")

t=(1,2,2,3,2,4)
print(t.index(2))
print(t.count(2))
