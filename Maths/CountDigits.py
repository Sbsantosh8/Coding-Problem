
def CountDig(n):
    a = str(n)
    count = len(a)
    return count

res = CountDig(10)
print(res)



def CountDig1(n):
    count = 0
    while n >0:
        n = n //10
        count +=1
        
    return count    

res1 = CountDig1(10)
print(res1)
        