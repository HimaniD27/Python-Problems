def removeCharacters(string):
  new_string=''
  for i in range(len(string)):
    if (ord(string[i])>=65 and ord(string[i])<=90) or (ord(string[i])>=97 and ord(string[i])<=122):
      new_string+=string[i]
  return new_string
print(removeCharacters("pi==3.14 and phi==1.618"))  




inp_str=input()
out_str=''
for i in inp_str:
  if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
    out_str+=i
print(out_str)


