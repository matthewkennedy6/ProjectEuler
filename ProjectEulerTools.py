import math


def isPrime(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return 0
    return 1


def primesToN(N):
    primes = [2]
    for i in range(3, N+1, 2):
        isprime = 1
        for j in range(2, int(math.sqrt(i))):
            if i % j == 0:
                isprime = 0
        if isprime:
            primes.append(i)
    return primes


def NPrimes(N):
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    i = 1

    while len(primes) < N:
        j = 23
        if isPrime(j):
            primes.append(j)

    return primes


def isPalindrome(str):
    for i in range(math.floor(len(str))):
        if str[i] != str[-1 - i]:
            return 0

    return 1

