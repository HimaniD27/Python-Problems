def smallest_element(arr):
  min_ele=arr[0]
  for i in range(len(arr)):
    if arr[i]<min_ele:
      min_ele=arr[i]
  return min_ele

print(smallest_element([4,3,8,-20,1,7,0,-1,9]))