from numpy import *

mw = zeros((21, 21), dtype=int)


def matrix_way(n, m):
    if n<m:
        n,m = m,n
    
    if mw[n,m]!=0:
        return mw[n,m]
    
    if m==1:
        return n+1
    
    print n,m
    mw[n,m] = matrix_way(n-1, m) + matrix_way(n, m-1)
    return mw[n,m]


solution = matrix_way(20, 20)

print(solution)
