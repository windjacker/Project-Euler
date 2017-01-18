def fac(n):
    f = 1
    for i in range(n,1,-1):
        f *= i
    
    return f



solution = 0

m = [i for i in range(10)]
n = 10**6


def lex(m, n):
    """
       returns the n-th lexicographic permutation of the m digits
    """
    
    perm = []
    
    while (len(m)>1):
        print perm, m
        for k in range(len(m)):
            print (fac(len(m)-1)*(k+1)), n
            if (fac(len(m)-1)*(k+1))>=n:
                perm.append(m[k])
                n -= fac(len(m)-1)*(k)
                m.pop(k)
                break
    
    perm.extend(m)
    
    print perm
    
    return perm



solution = lex([0,1,2], 6)
solution = lex(m, n)


print(solution)
