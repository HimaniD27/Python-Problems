arr=[2,5,9,8,5]
for num in arr:
    print(num)






arr=[2,5,9,8,5]
for i in range(len(arr)):
    print(arr[i])






def return_elements(arr):
    elements=[]
    for i in range(len(arr)):
        elements.append(arr[i])
    return elements

print(return_elements([2,5,9,8,5]))

