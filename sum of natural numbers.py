def sumNaturalNumbers(n):     #using recursion
  if n==1:
    return 1
  return n+sumNaturalNumbers(n-1)     #recursion

print(sumNaturalNumbers(3))      




def sum_of_naturals(n):
  result=0
  for i in range(1,n+1):
    result+=i
  return result

print(sum_of_naturals(3))