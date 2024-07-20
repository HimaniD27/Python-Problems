# Given an integer N, find the largest integer M such that M<N and the sum of the digits of M is smaller than N

def max_digitsum(n):
    num=str(n)
    
    option_1=str(int(num)-1)
    
    sum_option1=0
    for i in range(len(option_1)):
        sum_option1+=int(option_1[i])
    
    
    option_2=""
    
    for digit in range(len(num)):
        if digit==0:
            zeroth_ind=str(int(num[0])-1)
            option_2+=zeroth_ind
        else:
            option_2+=('9')
    
    sum_option2=0
    for i in range(len(option_2)):
        sum_option2+=int(option_2[i])
    

#     print(option_1)
#     print(sum_option1)
#     print(option_2)
#     print(sum_option2)
    

    if sum_option1>sum_option2:
        print(option_1)
    elif sum_option2>sum_option1:
        print(option_2)
    elif sum_option1==sum_option2:
        if int(option_1)>int(option_2):
            print(option_1)
        elif int(option_2)>int(option_1):
            print(option_2)


max_digitsum(2800)




#or
def max_digitsum(n):
    num = str(n)
    
    option_1 = str(int(num) - 1)
    sum_option1 = sum(int(digit) for digit in option_1)

    option_2 = str(int(num[0]) - 1) + '9' * (len(num) - 1)
    sum_option2 = sum(int(digit) for digit in option_2)
    
    if sum_option1 > sum_option2:
        return option_1
    elif sum_option2 > sum_option1:
        return option_2
    else:
        if int(option_1) > int(option_2):
            return option_1
        else:
            return option_2

print(max_digitsum(899))  
