#leap year = all the years completely divisible by 4 but not by 100, all the years completely divisible by 400

def isLeap(year):
  year=int(year)
  if year%400==0 or (year%4==0 and year%100!=0):
    print("It is a leap year")
  else:
    print("It is not a leap year")

isLeap(2000)