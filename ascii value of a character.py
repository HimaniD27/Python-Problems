character=input()
ascii_val=ord(character)     #ord() expects character, not string
print(ascii_val)

# The ASCII value of a character is its numerical representation in the ASCII (American Standard Code for Information Interchange) table. ASCII is a character encoding standard used for representing text in computers and other devices that use text. Each character (such as letters, digits, punctuation marks, and control characters) is assigned a unique 7-bit or 8-bit binary number.
# Important ASCII values:
# A-Z=65-90
# a-z=97-122
# 0=48
# 0-9=48-57
# space ' '=32
# printable characters(space-at sign @)= 32-64
# underscore _=95
# pipe |-124
# backslash \ =92
# {,}=123,125
# [,]=91,93
# tilde ~=126
# caret/circumflex ^=94

# The ord() function in Python returns the Unicode code point (i.e., the integer value) of a single character.
# A Unicode code point is a numerical value that uniquely identifies each character in the Unicode character set. Unicode is a universal character encoding standard that encompasses virtually all characters and symbols from all the writing systems of the world, as well as technical symbols, punctuation, and other text elements.