'''
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
'''
from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))) - {1, n}

def isPrime(n):
    result = True
    for i in range(2, int(n**0.5)+1, 1):
        if n % i ==0:
            result = False
            break
    return result

def primeFactors(n):
    my_list = factors(n)
    new_set =set()
    for eachNumber in my_list:
        if isPrime(eachNumber):
            new_set.add(eachNumber)
    return new_set

def DistinctPrimeFactors():
    my_number = 1
    while True:
        if len(primeFactors(my_number)) == 4 and len(primeFactors(my_number+1)) == 4 and len(primeFactors(my_number+2)) == 4 and len(primeFactors(my_number+3)) == 4:
            break
        my_number += 1
    return my_number



    # n is the number of distinct prime numbers
final = DistinctPrimeFactors()
#final = primeFactors(644)
#final = isPrime(4)
#final = factors(14)
print(final)