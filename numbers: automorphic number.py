# Automorphic numbers are numbers whose squares end with the number itself. Ex:5,6,25,76

def is_automorphic(num):
  number=str(num)
  square=str(num**2)
  return square.endswith(number)
test_numbers=[5,6,10,25,11,76,47]
automorphic_numbers=[num for num in test_numbers if is_automorphic(num)]
print(automorphic_numbers)


# [num for num in test_numbers if is_automorphic(num)]: 

# This is a list comprehension that creates a new list containing only the automorphic numbers from test_numbers

# Components of the List Comprehension

# Iteration:
# for num in test_numbers: This part iterates over each element in the test_numbers list. Here, test_numbers is the list [5, 6, 10, 25, 11, 76, 47].
# Condition:
# if is_automorphic(num): This part is a conditional statement that checks if the current number num is automorphic by calling the is_automorphic(num) function. If the condition is true, the number num is included in the new list. If the condition is false, the number is not included.
# Output Expression:
# num: This specifies what should be included in the new list. In this case, it is the number num itself, provided it meets the condition.