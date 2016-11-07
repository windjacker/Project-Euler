n = 3


for x in [999]: #range(10**(n-1),0,-1):
    for y in [999]: #range(10**(n-1),0,-1):
        solution = True
        xv = [0 for i in range(2*n+1)]
        yv = [0 for i in range(2*n+1)]
        zv = [0 for i in range(2*n+1)]

        for i in range(n):
            xv[i] = int( (x%10**(i+1))/10**i )
            yv[i] = int( (y%10**(i+1))/10**i )

        print(xv, yv)

        for i in range(2*n+1):
            zv[i] = 0
            for j in range(i+1):
                zv[i] += (xv[j]*yv[i-j])%10
            for j in range(i):
                zv[i] += int( (xv[j]*yv[i-j-1])/10 )

        print(zv)

        for i in range(n):
            if zv[i]!=zv[-i]:
                solution = False

        if solution:
            print(zv)
            break
