solution = 0

i = 2

a = 1
b = 1

while(a < 10**(1000-1)):
    a, b = a+b, a
    i += 1

solution = i

print("F_{} = {}".format(solution, a))
