N = 100
factors = []

plist = []
isprime = True

l = [2]
m = list(range(3, int(N/2), 2))
print(l)
print(m)
o = l.extend(m)
print(o)
for i in [2]:
    isprime = True
    
    for p in plist:
    #    print(i, p, i%p==0)
        if i%p==0:
            isprime = False
            break

    if isprime:
        #print(i)
        plist.append(i)
        

        while(N%i==0):
            factors.append(i)
            print(N, i)
            if N==i:
                break
            else:
                N /= i
        else:
           # print(i)
            if i>N/2:
                break

#print(plist)
print(factors)