
def isSumPalindrome(n):
    

    for _ in range(5):
        rev = 0
        temp = n
        while temp > 0:
            digit = temp % 10
            rev = rev * 10 + digit
            temp //= 10

        if n == rev:
            return n

        n += rev

    return -1
    
    
n = (input())

arr = n.split()

res = isSumPalindrome(int(arr[-1]))

print(res)
