from functions import isPandigital, divisors, digits

solution = 0

for n in range(1000, 10000):
    for a in divisors(n):
        b = n/a
        
        d = digits(a)
        d.extend(digits(b))
        d.extend(digits(n))
        
        if (len(d) == 9) and isPandigital(d):
            print "{} * {} = {}".format(a, b, n)
            solution += n
            break



print(solution)
