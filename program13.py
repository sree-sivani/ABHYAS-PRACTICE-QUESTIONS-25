n = int(input())
rev_num = 0
while (n > 0):
    digit = n % 10
    rev_num = rev_num * 10 + digit
    n //= 10

print(rev_num)
