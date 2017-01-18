primarr = [2]
i = 3

while len(primarr)<=10001:
	for k in primarr:
		if i%k==0:
			break
	else:
		primarr.append(i)
	i += 2
	if len(primarr)%500==0:
		print(len(primarr))


solution = primarr[10000]

print(solution)
