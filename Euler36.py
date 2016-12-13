from functions import isPalindrom, binary


solution = 0

for n in range(1, 10**6):
    if isPalindrom(n) and isPalindrom(binary(n)):
        solution += n

print(solution)
