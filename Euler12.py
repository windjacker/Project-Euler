from factorize import *

solution = 0

solved = False
i = 1
tsum = 0

while( solved==False ):
    tsum += i
    
    if len(divisors(tsum)) > 500:
        solved = True
    
#    print(i)
    i += 1


solution = tsum

print(solution)
