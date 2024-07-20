# https://www.geeksforgeeks.org/largest-number-not-greater-than-n-all-the-digits-of-which-are-odd/?ref=ml_lbp
# Largest number not greater than N all the digits of which are odd

def allOddDigit(n):
    num=str(n)
    answer=""
    b=0
    
    for index,digit in enumerate(num):
        
        if int(digit)%2!=0:
            answer+=digit
        
        if int(digit)%2==0 and digit!='0':
            answer+=str(int(digit)-1)
            b=index+1
            break
    
        if digit=='0':
            answer=str(int(answer)-2)
            int(answer)
            b=index
            print(b)
            break

    for i in range(b,len(num)):
        print('i=',i)
        answer+='9'
    print(answer)
    
allOddDigit(7308)
allOddDigit(7208)
allOddDigit(7108)
allOddDigit(7343)




#or
def fun(n):
    nums = []
    while n>0:
        nums.append(n%10)
        n = n//10
    nums.reverse()
    print(nums)
    b = 1000
    for i in range(len(nums)):
        if(nums[i]%2==0):
            b = i
            break
    print(b)
    finalAns = 0
    i = 0
    while i<min(len(nums),b):
        finalAns= finalAns*10+nums[i];
        i +=1
    print(finalAns)
    if b<len(nums):
        if(nums[b]==0):
            finalAns-=2;
            while b<len(nums):
                finalAns = finalAns*10+9
                b +=1
        else:
           finalAns = finalAns*10+nums[b]-1;
           b+=1 
           while b<len(nums):
                finalAns = finalAns*10+9
                b +=1 
    return finalAns


print(fun(7373))
