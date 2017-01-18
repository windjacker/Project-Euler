def fac(n):
    if n == 0:
        return 1
    if n == 0:
        return 1
    f = 1
    for i in range(2, n+1):
        f *= i
    return f


solution = 0

for i in range(10, 10**6):
    s = str(i)
    tmp = sum(fac(int(item)) for item in s)
    if tmp==i:
        solution += i



print("solution= {}".format(solution))
