def oddNumberSeries(n):     #first n odd numbers
    series=[]
    for i in range(n):
        series.append(2*i+1)
    return series

print(oddNumberSeries(10))




for n in range(5):    #for first 5 numbers
    print(2*n+1)