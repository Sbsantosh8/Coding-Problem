
'''Naive Method'''

def SumNat(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return sum


res = SumNat(10)
print(res)



'''Efficient Method'''

def SumNat1(n):
    return (n*(n+1))//2


res1 = SumNat1(10)
print(res1)
    