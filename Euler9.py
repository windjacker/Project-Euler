for c in range(1, 1000):
	for a in range(1, 1000-c):
		b = 1000-a-c
		if a**2+b**2==c**2:
			print(a,b,c)
			solution = a*b*c
			break


print(solution)
