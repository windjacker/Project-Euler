from numpy import sqrt

def isPrime(n):
    if (n<0):
        return False
    if (n%2==0):
        return False
    for i in range(3, int(sqrt(n))+1, 2):
        if (n%i==0):
            return False
    
    return True

def formulaCount(a, b):
    n = 0
    while( isPrime(n*n+a*n+b) ):
        n += 1
    
    return n


solution = 0, 0
count = 0

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        tmp = formulaCount(a, b)
        if (tmp>count):
            count = tmp
            solution = a, b


print("a= {}, b= {}, c= {}: solution= {}".format(solution[0], solution[1], count, solution[0]*solution[1]))
