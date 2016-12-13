from functions import isPrime

def truncatable(n, direction):
    """
       Creates all truncatable numbers fo rone direction.
       Args:    Number n
                direction char 'l'/'r'/'b'
       Return:  Array of all directional truncatable Numbers
       Example: truncatable( 3797, 'l' ) = [3797, 797, 97, 7]
                truncatable( 3797, 'r' ) = [3797, 379, 37, 3]
                truncatable( 3797, 'b' ) = [3797, 797, 379, 97, 37, 7, 3]
    """
    r = [int(n)]
    n = str(n)
    for i in range(1, len(n)):
        if direction=='r':
            r.append( int(n[:-i]) )
        elif direction=='l':
            r.append( int(n[i:]) )
        elif direction=='b':
            r.append( int(n[i:]) )
            r.append( int(n[:-i]) )
    
    return r


solution = 0

primes = file('Primzahlen.txt', 'r')

count = 11
for n_ in primes:
    n = int(n_[:-1])
    if n<10:
        continue
    if all([isPrime(i) for i in truncatable(n, 'b')]):
        print n
        solution += n
        count -= 1
    if count==0:
        break


print(solution)
