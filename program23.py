def count_primes(n):
    if n <= 1:
        return 0

    prime_count = 0
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_count += 1

    return prime_count

T = int(input())

for _ in range(T):
    N = int(input())
    result = count_primes(N)
    print(result)
