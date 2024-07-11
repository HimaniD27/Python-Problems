# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with 6 places after the decimal.
# https://www.hackerrank.com/challenges/one-month-preparation-kit-plus-minus/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one

def plusMinus(arr):
    a=0
    b=0
    c=0
    for i in arr:
        if i>0:
            a+=1
        elif i<0:
            b+=1
        else:
            c+=1
    print("{:.6f}".format(a/(a+b+c)))
    print("{:.6f}".format(b/(a+b+c)))
    print("{:.6f}".format(c/(a+b+c)))