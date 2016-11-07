squareSum = 0
sumSquare = 0

for i in range(1,101):
	squareSum += i*i
	sumSquare += i

sumSquare *= sumSquare

solution = sumSquare - squareSum


print(solution)
