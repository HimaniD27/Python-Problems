def primeFactors(num):
  divisor=2 
  factors=[]
  while divisor<=num:
    if num%divisor==0:
      factors.append(divisor)
      num=num//divisor
    else:
      divisor+=1
  return factors

print(primeFactors(90))
    