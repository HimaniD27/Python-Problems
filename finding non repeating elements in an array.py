def nonRepeating(arr):
  d={}
  for ele in arr:
    if ele in d:   #d[ele]=d.get[ele,0]+1
      d[ele]+=1
    else:
      d[ele]=1
  
  non_repeating_elements=[ele for ele,count in d.items() if count==1]
  return non_repeating_elements

print(nonRepeating(["a","b",1,7,9,9,0,6,"b","c",1,True,False]))


# if False is present in the array, it will be counted as 0
# if True is present in the array, it will be counted as 1
# if True/False- not present in the array, it will be counted as 1/0 and vice-versa

