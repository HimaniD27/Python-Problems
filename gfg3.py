# https://www.geeksforgeeks.org/largest-even-digit-number-not-greater-n/?ref=ml_lbp
# Largest even digit number not greater than N

def allEvenDigit(n):
    num=str(n)
    answer=""
    a=0
    
    for index,value in enumerate(num):
        
        if int(value)%2==0:
            answer+=value
            a=index+1
        #print(answer)
        
        if int(value)%2!=0:
            answer+=str(int(value)-1)
            a=index+1
            break
        #print(answer)
        
    for i in range(a,len(num)):
        answer+='8'
    print(answer)   

allEvenDigit(6208)
allEvenDigit(6428)
allEvenDigit(6328)
allEvenDigit(6308)
allEvenDigit(1109)
allEvenDigit(7109)
