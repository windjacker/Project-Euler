n = 3


for x in range(10**(n)-1,10**(n)-10**(n-1),-1):
    solution = True
    for y in range(x-1,10**(n)-10**(n-1),-1):
        solution = True
        zv = [0 for i in range(2*n)]
        z = x*y

        for i in range(2*n):
            zv[i] = int( (z%10**(i+1))/10**i )

        for i in range(n):
            if zv[i]!=zv[-(i+1)]:
                solution = False

        if solution:
            print(z, ' = ', x, ' * ', y)
            break
    
    if solution:
        break
