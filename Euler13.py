solution = 0

# read numbers
data = file('Euler13.dat')
numbers = []
for i in data:
    numbers.append( int(i[:-1]) )


# first 10 digits of sum
for i in numbers:
    solution += i#nt( i/(10**39) )


print(solution)
