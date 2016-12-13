from numpy import sqrt

def isPrime(n):
    if n%2==0:
        return False
    for i in range(3, int(sqrt(n))+1, 2):
        if n%i==0:
            return False
    return True

def permutations(n):
    r = []
    s = str(n)
    for i in range(len(s)):
        r.append( int(s[i:]+s[:i]) )
    return r


solution = 0

for i in range(10**6):
    if all(isPrime(item) for item in permutations(i)):
        solution += 1


print("solution= {}".format(solution))
