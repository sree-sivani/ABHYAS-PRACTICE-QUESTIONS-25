def sumOfDigits(N):
    

    sum = 0
    while N > 0:
        digit = N % 10
        sum += digit
        N //= 10

    return sum
    
n = int(input())
res = sumOfDigits(n)

print(res)
