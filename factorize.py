#!/usr/bin/env python

def factorize(n):
    """
       Return the primefactors of n and their exponent as an list of
       tupels.

       Args:    Number n
       Return:  list of sorted 2-tupels with primefactor and exponent

       Example: factorize(2016)
                [(2, 5), (3, 2), (7,1)]
    """
    data = open('Primzahlen.txt')
    primarr = []

    for i in data:
        primarr.append(int(i[:-1]))

    n_fac = []
    for p in primarr:
        count = 0
        while n%p==0:
            n /= p
            count += 1
        if count!=0:
            n_fac.append( (p, count) )
        if n==1:
            break

    return n_fac

def divisors(n):
    """
       Return the divisors of n as an list.

       Args:    Number n
       Return:  list of divisors, sorted

       Example: 
    """
    div = []
    n_fac = factorize(n)

    for p in n_fac:
        for i in range(p[1]+1):
            div.append(p[0]**i)
    
