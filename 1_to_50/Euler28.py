solution = 0
n = 1001
last = 0

for i in range(1, n+1, 2):
    #print "n= ", i
    if (i==1):
        last = 1
        solution += last
    else:
        for k in range(4):
            last += i-1
            solution += last
            #print "last= ", last


print("solution= {}".format(solution))
