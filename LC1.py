# https://leetcode.com/problems/two-sum/description/

# TC=O(n)
def two_sum(nums,target):
  d={}
  for i,num in enumerate(nums):
    complement=target-num
    if complement in d:
      return [d[complement],i]
    d[num]=i
  return []

print(two_sum([2,7,11,15],9))




# TC=O(n**2)
def two_sum(num,target):
  n=len(num)
  for i in range(n):
    for j in range(i+1,n):
      if num[i]+num[j]==target:
        return[i,j]
  return []

print(two_sum([2,7,11,15],9))