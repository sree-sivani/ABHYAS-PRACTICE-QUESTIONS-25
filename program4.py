def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def sum_of_primes_in_range(start, end):
    prime_sum = 0
    for num in range(start, end + 1):
        if is_prime(num):
            prime_sum += num
    return prime_sum

start_range = int(input())
end_range = int(input())

result = sum_of_primes_in_range(start_range, end_range)
print(result)
