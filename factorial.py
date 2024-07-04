def findFactorial(num):
  result=1
  if num<0:
    return None
  for i in range(1,num+1):
    result*=i
  return result
print(findFactorial(6))



def factorial(n):    #using recursion
  if n==1:
    return 1
  return n*factorial(n-1)
print(factorial(6))
  