# 1929 문제 풀이
import sys
input = sys.stdin.readline

def sieve_of_Eratosthenes(n):
    a = [False, False] + [True] * (n - 1)
    primes = []

    for i in range(1, n + 1):
        if a[i]:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                a[j] = False
    return primes

m, n = map(int, input().split())

primes = sieve_of_Eratosthenes(n)
for prime in primes:
    if prime >= m:
        print(prime)

