word="python"
print(len(word))
print(word[0])

word1 = "I love"
word2 = "python"
sentence = word1 + " " + word2
print(sentence)

for ch in word:
    print(ch)


'''Slicing in strings'''
print(word[2:4])

str= "I study from ApnaCollege"
print(str[:])

print(word[-4:-2])

'''String Formating'''
a=5
b=10
sum=a+b
# normal formatting
print("Language is {}".format("Python"))
print("Sum of {} and {} is {}".format(a, b, sum))

#index based formatting
print("Sum of {1} and {0} is {2}".format(a, b, sum))

#value based formatting
print("{a} values of vars {a} and {b}".format(a=5, b=10))


'''f-strings'''
print(f"Average of {a} and {b} is {a+b/2}")