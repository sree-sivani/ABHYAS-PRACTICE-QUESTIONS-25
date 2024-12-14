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

def smallest_prime_in_range(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            return num
    return -1  

start_range = int(input())
end_range = int(input())

smallest_prime = smallest_prime_in_range(start_range, end_range)
if smallest_prime != -1:
    print(smallest_prime)
# else:
#     print("NO")
