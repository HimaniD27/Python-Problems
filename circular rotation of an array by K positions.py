def arrayRotation(arr,k):
  k=k%len(arr)    #By using k % len(arr), we reduce unnecessary full-length rotations #rotating by k and k%len(arr) results in the same string
  arr[:]=arr[-k:]+arr[:-k]
  return arr

print(arrayRotation([2,3,4,5],2))




arr,k=input(),int(input())
# arr=input()
# k=int(input())
k=k%len(arr)
arr=arr[-k:]+arr[:-k]
print(arr)