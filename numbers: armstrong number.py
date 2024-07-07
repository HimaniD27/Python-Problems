# An Armstrong number, also known as a narcissistic number, is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
#a number n with d digits is an Armstrong number if the sum of its digits each raised to the power of d is equal to n.
#ex:153,1634

def isArmstrong(n):
  digits=len(str(n))
  check_sum=[]
  for digit in str(n):
    sq=int(digit)**digits
    check_sum.append(sq)
  if sum(check_sum)==n:
    print("armstrong")
  else:
    print("armweak")

isArmstrong(153)


        

def isArmstrong(n):
  digits=len(str(n))
  check_sum=sum(int(digit)**digits for digit in str(n))  #list comprehension
  if check_sum==n:
    print("armstrong")
  else:
    print("armweak")

isArmstrong(153)