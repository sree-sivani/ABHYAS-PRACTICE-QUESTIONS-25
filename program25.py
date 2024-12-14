def is_palindrome(num):
    
    original_num = num
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10

    return original_num == reversed_num

num = int(input())

if is_palindrome(num):
    print("YES")
else:
    print("NO")
