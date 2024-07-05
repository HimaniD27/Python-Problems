#palindrome for strings having upper,lowercase letters and other characters

def isPalindrome(string):
    string0 = string.lower()
    def helper(s):
        cleaned = []
        for char in s:
            if 'a' <= char <= 'z' or '0' <= char <= '9':
                cleaned.append(char)
        return ''.join(cleaned)
    
    cleaned_string = helper(string0)
    for i in range(len(cleaned_string) // 2):
        if cleaned_string[i] != cleaned_string[len(cleaned_string) - i - 1]:
            return "no"
    return "yes"

print(isPalindrome("A man, a plan, a canal, Panama!"))  




def is_palindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())   
    return cleaned == cleaned[::-1]
s = "A man, a plan, a canal, Panama!"
print(is_palindrome(s))  

# char.isalnum() checks if the character is alphanumeric (letters and numbers only). 
# join function combines all these lowercased alphanumeric characters into a single string without spaces or punctuation.




# using string module
import string
def is_palindrome(s):
    translator = str.maketrans('', '', string.punctuation)
    cleaned = s.translate(translator).replace(" ", "").lower()
    return cleaned == cleaned[::-1]

s = "A man, a plan, a canal, Panama!"
print(is_palindrome(s))  

# str.maketrans(x, y, z)
# x: This is a string where each character in the string is mapped to the character at the same position in the second parameter. If the first parameter is empty, it means no characters are mapped to others.
# y: This is a string of characters that will replace the characters in the first parameter. If the second parameter is empty, no characters are mapped to others.
# z:  This is a string of characters that should be deleted from the string when using the translation table. In this case, string.punctuation is passed as the third parameter, indicating that all punctuation characters should be removed from the string

# translator : creates a translation table (translator). This will specify that every punctuation character in string.punctuation should be removed from the string when you call s.translate(translator).

# The str.translate() method is used to apply the translation table created by str.maketrans() to a string. This method replaces or removes characters in the string based on the translation table.
# s.translate(translator): This method translates the string s using the translation table translator created earlier. It removes all punctuation characters from s.