# finding nth fibonacci number
# using recursion

def fibo(n):
  if n<0:
    print("invalid input")
  elif n==0:
    return 0
  elif n==1:
    return 1
  else:
    return fibo(n-1)+fibo(n-2)

print(fibo(10))




# recursion:
def fib(n):
    print("Called fib(",n,")")
    if n==0:
        print ("Returned fib(0)")
        return 0
    if n==1:
        print ("Returned fib(1)")
        return 1
    print ("Calling fib for n=",n, "sending call to",n-1, "and",n-2)
    a = fib(n-1) +fib(n-2)
    print ("Returned fib(",n,") ")
    #print ("Got the result back from"‚n-1,"and", n-2)
    return a
print (fib(6))




# dynamic programming
def fib(n,dp):
    print("Called fib(",n,")")
    if n==0:
        print("Returned fib(0)")
        return 0
    if n==1:
        print("Returned fib(1)")
        return 1
    if n in dp:
        print("Returned fib(",n,")")
        return dp. get (n, 0)
    print ("Calling fib for n=",n, "sending call to",n-1, "and",n-2)
    a = fib(n-1, dp) +fib (n-2, dp)
    dp[n] = a
    #print ("Got the result back from",n-1,"and", n-2)
    print( "Returned fib(",n,")")
    return dp[n]

dp= {}
print (fib (6, dp))