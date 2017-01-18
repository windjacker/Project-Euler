solution = 0

n = 2**1000

n_str = str(n)
for i in n_str:
    solution += int(i)

print(solution)
