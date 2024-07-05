def isPalindrome(string):
  return string==string[::-1]

def isLongestPal(arr):
  longest=''
  for str1 in arr:
    s=str(str1)
    if isPalindrome(s) and len(s)>len(longest):
      longest=s
  return longest

print(isLongestPal(["radar","madam","India",1234321]))

