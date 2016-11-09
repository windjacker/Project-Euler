n = 3


for x in range(10**(n)-1,900,-1):
    solution = True
    for y in range(x-1,900,-1):
        solution = True
        zv = [0 for i in range(2*n)]
        z = 987654#x*y

        for i in range(2*n):
            zv[i] = int( (z%10**(i+1))/10**i )

        for i in range(n):
            if zv[i]!=zv[-i-1]:
                solution = False

        if solution:
            print(z, zv)
            print(zv[0],zv[1],zv[2], zv[-3], zv[-2], zv[-1])
            break
    
    if solution:
        break
