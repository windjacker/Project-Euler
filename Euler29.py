solution = 0
n = 100
listed = []

for a in range(2, n+1):
    for b in range(2, n+1):
        pw = a**b
        if all( (pw != item) for item in listed ):
            listed.append(pw)

solution = len(listed)

print("solution= {}".format(solution))
