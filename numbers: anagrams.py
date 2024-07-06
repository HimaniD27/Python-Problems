# Anagrams are words or phrases formed by rearranging the letters of another word or phrase, typically using all the original letters exactly once. For example, the word "listen" can be rearranged to form the word "silent".

def areAnagrams(str1,str2):
  str1=str1.replace(" ","").lower()
  str2=str2.replace(" ","").lower()
  if len(str1)!=len(str2):
    print("no")
  else: 
    if sorted(str1)==sorted(str2):
      print("yes") 
    else:
      print("no")

areAnagrams("listen","silent")