print(pow(2,3))  #built-in fn. = pow(base,exponent)




number=float(input())
power=int(input())
def calculatePower(number,power):
  result=1
  for _ in range(power):
    result*=number
  return result
print(calculatePower(number,power))

# _ : a common convention in Python used to indicate that the variable is a placeholder and its value will not be used inside the loop. It is used when you need a loop variable but do not intend to use it in the loop body.

# for _ in range(power): execute the following block of code power times. The underscore _ is used to indicate that the loop variable is not important and will not be used in the loop's body.
