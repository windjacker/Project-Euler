from factorize import *


def isAbundant(n):
    return sum(divisors(n)[:-1])>n




solution = 0
a = []

for i in range(1, 28123+1):
    for n in a:
        if isAbundant(i-n):
            #print("{} = {}+{}".format(i, n, i-n))
            break
    else:
        solution += i
        print i
    if isAbundant(i):
        a.append(i)


print(solution)
