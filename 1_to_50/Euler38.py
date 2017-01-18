from functions import digits, isPandigital, skalarProd, integer

solution = 0


p = [1, 2, 3, 4, 5, 6, 7, 8, 9]
p = unsort(p)



for n in range(1, 10**6):
    print n
    for i in range(2, 9):
        p = skalarProd(n, range(1, i+1))
        d = []
        for tmp in p:
            d.append(tmp)
        d = integer(d)
        if d>987654321:
            break
        if len(digits(d))==9 and isPandigital(d) and d>solution:
            solution = d
            print n, i,  d

print(solution)
