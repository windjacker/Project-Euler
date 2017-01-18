def euler26(d):
    n = 1
    q = [(0, 1)]
    l = 0
    
    stop = False
    while(q[-1][1] > 0):
        n = q[-1][1]*10
        q.append( (int(n/d), n%d) )
        for i in range(len(q)-1):
            if (q[-1][1]==q[i][1]):
                stop = True
                l = len(q)-i-1
                break
        if stop:
            break
    
    return l



solution = 0


l = 0
for i in range(2, 1000):
    tmp = euler27(i)
    if (tmp > l):
        l = tmp
        solution = i


print(solution)
