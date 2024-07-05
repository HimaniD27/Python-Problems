def nonRepeating(string):
  string=string.lower()
  d={}
  for char in string:
    d[char]=d.get(char,0)+1
  non_repeating_chr=[char for char,count in d.items() if count==1]
  return non_repeating_chr

print(nonRepeating("TypeError"))