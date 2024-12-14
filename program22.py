def sum_even_digits(num):
   

    while num > 9:
        sum = 0
        while num > 0:
            digit = num % 10
            if digit % 2 == 0:
                sum += digit
            num //= 10
        num = sum

    return num
    
    
    
n = int(input())
ans = sum_even_digits(n)
print(ans)
