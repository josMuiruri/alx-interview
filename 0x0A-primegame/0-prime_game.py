#!/usr/bin/python3
'''Prime game
'''


def sieve_of_eratosthenes(max_n):
    """Generates prime numbers up to max_n using the Sieve of Eratosthenes."""
    primes = [True] * (max_n + 1)
    primes[0], primes[1] = False, False  # 0 and 1 are not primes
    p = 2
    while p * p <= max_n:
        if primes[p]:
            for i in range(p * p, max_n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(max_n + 1) if primes[p]]


def isWinner(x, nums):
    if not nums or x < 1:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_count = 0
        multiples_removed = [False] * (n + 1)

        for prime in primes:
            if prime > n:
                break
            if not multiples_removed[prime]:
                primes_count += 1
                for multiple in range(prime, n + 1, prime):
                    multiples_removed[multiple] = True

        if primes_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
