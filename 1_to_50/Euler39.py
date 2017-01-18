from numpy import sqrt

solution = 0

maxm = 0
for p in range(1000+1):
    count = 0
    for a in range(p):
        for b in range(a):
            if (p==a+b+sqrt(a*a+b*b)):
                count += 1
    
    if (count>maxm):
        maxm = count
        solution = p
    print p

print(solution)
