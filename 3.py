import ProjectEulerTools, math

N = 600851475143
primes = ProjectEulerTools.primesToN(int(math.sqrt(N)))

primeFactors = []

for prime in primes:
    while N % prime == 0:
        primeFactors.append(prime)
        N = N / prime

print(primeFactors)
