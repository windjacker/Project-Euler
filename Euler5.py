def integerFactorization(a):
	p_arr = []
	for p in [2,3,5,7,11,13,17,19]:
		count = 0
		while (a%p==0):
			count += 1
			a /= p
		p_arr.append( (p, count) )
	return p_arr


kgv_arr = [[2,0],[3,0],[5,0],[7,0],[11,0],[13,0],[17,0],[19,0]]
for a in range(2,21):
	a_primes = integerFactorization(a)
	for i in range(len(kgv_arr)):
		if a_primes[i][1]>kgv_arr[i][1]:
			kgv_arr[i][1] = a_primes[i][1]

solution = 1
for i in range(len(kgv_arr)):
	solution *= kgv_arr[i][0]**kgv_arr[i][1]
		

print(solution)
