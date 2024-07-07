# fibonacci series upto nth term

def fibo_series(n):
  series=[]
  a,b=0,1
  for i in range(n):
    series.append(a)
    a,b=b,a+b
  return series

print(fibo_series(10))




def fibo_series(n):
  if n<=0:
    return []
  elif n==1:
    return [0]
  series=[0,1]     #initializing the fibonacci series
  while n>len(series):
    series.append(series[-1]+series[-2])
  return series

print(fibo_series(10))

