# using built-in sort() : Modifies the original list and returns None.
# In-place Sorting: The sort() method sorts the list in place, meaning it modifies the original list.
# Return Value: It returns None.
# Usage: It is a method of list objects.

arr=[10,8,45,34,21,101]
arr.sort()                              #arr.sort(reverse=True)
print(arr)

arr=["z","o","y","x","i","q","a"]
arr.sort()                              #arr.sort(reverse=True)
print(arr)




# sorted() : Returns a new sorted list without modifying the original iterable.
# Returns a New List: The sorted() function returns a new list that is sorted, leaving the original list unchanged.
# Return Value: It returns a new sorted list.
# Usage: It can be used with any iterable (e.g., lists, tuples, strings, etc.).

arr=[10,8,45,34,21,101]
sorted_arr=sorted(arr)                  #sorted(arr,reverse=True)
print(sorted_arr)
#or simply
print(sorted(arr))

arr1=["z","o","y","x","i","q","a"]
sorted_arr1=sorted(arr1)                #sorted(arr1,reverse=True)
print(sorted_arr1)




def sortingFunction(arr):
    sorted_array=[]
    while arr:
        min_element=min(arr)
        sorted_array.append(min_element)
        arr.remove(min_element)
    return sorted_array

print(sortingFunction([10,8,45,34,21,101]))