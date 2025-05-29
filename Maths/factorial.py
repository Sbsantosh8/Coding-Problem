

# def fact(n):
#     res = 1
#     for i in range(1,n+1):
#         res = res * i
        
        
#     return res


# print(fact(5))  



# Recursive approach


def facto(n):
    if n == 0:
        return 1
    
    return n * facto(n-1)


print(facto(5))  