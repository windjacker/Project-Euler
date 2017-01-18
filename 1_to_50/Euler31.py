def coinCount(n, value):
    if value==7:
        return 1
    cc = 0
    coins = (200, 100, 50, 20, 10, 5, 2, 1)
    for i in range(int(n/coins[value])+1):
        #print n-i*coins[value], value+1
        cc += coinCount(n-i*coins[value], value+1)
    return cc

solution = coinCount(200, 0)


print("solution= {}".format(solution))
