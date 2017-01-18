def collatz(n):
    """
       return the next term in the Collatz-Sequenz
    """
    if n%2==0:
        return int(n/2)
    return 3*n+1




solution = 0
sol_count = 0

for i in range(10**6-1, 10**5, -1):
    count = 0
    n = i
    while(n!=1):
        n = collatz(n)
        count += 1
    
    if sol_count < count:
        solution = i
        sol_count = count
        print(i, sol_count, count)


print(solution)
