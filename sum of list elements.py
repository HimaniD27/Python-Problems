ls=[1,4,9,8,6,3]
total=sum(ls)   #using built-in function: sum()
print(total)
#or simply
print(sum([1,4,9,8,6,3]))




ls=[1,4,9,8,6,3]
total=0
for i in range(len(ls)):
    total+=ls[i]
print(total)




def totalOfElements(ls):
    total=0
    for i in range(len(ls)):
        total+=ls[i]
    return total
     
print(totalOfElements([1,4,9,8,6,3]))

