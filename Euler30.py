solution = 0


for i in range(2, 10**7):
    s = 0
    for d in str(i):
        s += int(d)**5
    if (i == s):
        solution += i
        print i


print("solution= {}".format(solution))
