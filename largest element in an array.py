def largest_element(arr):
  max_ele=arr[0]
  for i in range(len(arr)):
    if arr[i]>max_ele:
      max_ele=arr[i]
  return max_ele

print(largest_element([1,2,2,6,8,7,8,4,5]))