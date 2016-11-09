primarr = [2]
solution = 2

for i in range(3, 2000000, 2):
	if i%10000==1:
		print( (i/20000), "%")
	for k in primarr:
		if i%k==0:
			break
	else:
		primarr.append(i)
		solution += i


print(solution)
