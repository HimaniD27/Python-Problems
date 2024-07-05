# A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself.
# The smallest perfect number is 6.The first few perfect numbers are 6, 28, 496, and 8128.

def amIPerfect(num):
  divisors=[]
  for i in range(1,num):
    if num%i==0:
      divisors.append(i)
  if sum(divisors)==num:
    print("You are just perfect. But careful! Don't be arrogant about it ever.")
  else: 
    print(f"Aww... Dont be sad Number {num}. You are not imperfect, you just need to do a little work on your self.")
  
amIPerfect(28)