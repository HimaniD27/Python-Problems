def reverse_number(n):
  number=str(n)
  result=""
  for i in range(len(number)):
    result=number[i]+result
  return int(result)

print(reverse_number(4567))




def reverse_number(n):
  number=str(n)
  reverse=number[::-1]
  return int(reverse)
print(reverse_number(4567))
#or
number=str(input())
reverse=number[::-1]
print(int(reverse))




#when we divide a number by 10, the remainder is always the last digit
number=int(input())
reverse=''
while number>0:
  remainder=number%10
  reverse=reverse+str(remainder)
  number=number//10
print(int(reverse))

#reverse.append(remainder) is wrong  
#The append method is used to add an element to the end of a list, but strings in Python do not have an append method because they are immutable. Instead, you can concatenate strings using the + operator or by using other string methods.




number=int(input())
reverse=0
while number>0:
  remainder=number%10
  reverse=(reverse*10)+remainder
  number=number//10
print(int(reverse))