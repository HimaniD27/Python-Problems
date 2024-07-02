def reverse_string(string):
    reversed=string[::-1]        #using slicing
    return reversed

print(reverse_string("mountainK2"))




#To reverse a string in Python using the built-in reverse() function, you actually need to reverse a list of characters first since reverse() is a method for lists
string="mountain"
list_str=list(string)
list_str.reverse()
reversed_string=''.join(list_str)
print(reversed_string)




def reverse_string(string):
    reversed=''
    for i in range(len(string)):
        reversed=string[i]+reversed
    return reversed

print(reverse_string("mountain"))



