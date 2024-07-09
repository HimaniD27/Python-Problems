def binary_to_decimal(binary_num):
  decimal=0
  binary_num=binary_num[::-1]
  for i in range(len(binary_num)):
    if binary_num[i]=="1":
      decimal+=2**i
    elif binary_num[i]!="0":
      return "invalid number"
  return decimal

print(binary_to_decimal("1101"))




