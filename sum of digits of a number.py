def sumOfDigits(num):
    sum_of_digits=0
    for i in range(len(num)):
        sum_of_digits+=int(num[i])
    return sum_of_digits
print(sumOfDigits("124567"))

# objects of type "int" : do not have len(), are not subscriptable
# In Python, you can use subscripting(indexing or slicing) on sequences like strings, lists, or tuples, but not on integers.




number=input()
sum=0
for digit in number:
    sum+=int(digit)
print(sum)