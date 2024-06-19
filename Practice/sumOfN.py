import math
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors

def sum_of_primes_up_to(n):
    sum_primes = 0
    for i in range(2, n + 1):
        if is_prime(i):
            sum_primes += i
    return sum_primes
    
k = 2
factors = prime_factors(k)
min_prime = min(factors)
sum_primes = sum_of_primes_up_to(min_prime)
print(k * sum_primes)
