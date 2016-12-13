#!/usr/bin/env python

from numpy import *

def factorize(n):
    """
       Return the primefactors of n and their exponent as an list of
       tupels.
       Args:    Number n
       Return:  list of sorted 2-tupels with primefactor and exponent
       Example: factorize( 2016 ) = [(2, 5), (3, 2), (7,1)]
    """
    n_fac = []
    
    # modulo 2
    k = 2
    count_k = 0
    while n%k==0:
        n /= k
        count_k += 1
    if count_k!=0:
        n_fac.append( (k, count_k) )
    if n==1:
        return n_fac
    
    # modulo 3+2*...
    for i in range(3,n+1,2):
        count = 0
        while n%i==0:
            n /= i
            count += 1
        if count!=0:
            n_fac.append( (i, count) )
        if n==1:
            break

    return n_fac

def divisors(n):
    """
       Return the divisors of n as an list.
       Args:    Number n
       Return:  list of divisors, sorted
       Example: divisors( 70 ) = [1, 2, 5, 7, 10, 14, 35, 70]
    """
    n_fac = factorize(n)

    dt = array(1)
    for p in n_fac:
        dt = array( [dt * p[0]**i for i in range(p[1]+1)] )
    
    return sorted(dt.reshape(-1).tolist())


def binary(n):
    """
       Converts the given integer to binary.
       Args:    Number n
       Return:  n binary
       Example: binary( 35 ) = 100011
    """
    bn = []
    while(n!=0):
        bn.append(n%2)
        n = int(n/2)
    
    r = ''.join(map(str, [bn[-(i+1)] for i in range(len(bn))]))
    
    return int(r)
    

def isPalindrom(n):
    """
       Checks if the given number is a Palindrom
       (works for bases less than 10).
       Args:    Number n
       Return:  True/False
       Example: binary( 9016109 ) = True
    """
    nv = []
    while(n!=0):
        nv.append(n%10)
        n = int(n/10)
    
    nv2 = [nv[-(i+1)] for i in range(len(nv))]
    
    return nv==nv2


def isPrime(n):
    """
       Checks if the given number is prime.
       Args:    Number n
       Return:  True/False
       Example: isPrime( 1368491 ) = True
    """
    if n==0 or n==1:
        return False
    if n%2==0:
        return False
    for i in range(3, int(sqrt(n))+1, 2):
        if n%i==0:
            return False
    return True

def permutations(n):
    """
       Creates all permutations of the given number.
       Args:    Number n
       Return:  Array of integers
       Example: permutations( 197 ) = [197, 971, 719]
    """
    r = []
    s = str(n)
    for i in range(len(s)):
        r.append( int(s[i:]+s[:i]) )
    return r

