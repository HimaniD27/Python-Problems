# A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization). Some common examples include:
# Words: "radar," "level," "madam"
# Phrases: "A man, a plan, a canal, Panama!"
# Numbers: "121," "12321"

string=input()
reversed_string=string[::-1]
if string==reversed_string:
  print("Palindrome")
else:
  print("not a Palindrome")




def isPalindrome(string):
  for i in range(len(string)//2):
    if string[i]!=string[len(string)-i-1]:
      return "no"
  return "yes"

print(isPalindrome("radar"))

