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

def check_prime_numbers(arr, N):
  for i in range(N):
    if is_prime(arr[i]):
      print("PRIME")
    else:
      print("NOT")

N = int(input())
arr = []

for i in range(N):
  arr.append(int(input()))

check_prime_numbers(arr, N)
