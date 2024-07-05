def frequency_of_elements(arr):
  d={}
  for i in arr:
    d[i]=d.get(i,0)+1
  return d
      
print(frequency_of_elements([11,22,11,33,55,55,77,77,77]))
#'dict' object has no attribute 'append'




def calFreq(arr):
  d={}
  for char in arr:
    if char in d:
      d[char]+=1
    else:
      d[char]=1
  return d

print(calFreq([11,22,11,33,55,55,77,77,77]))