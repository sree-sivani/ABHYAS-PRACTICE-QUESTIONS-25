def is_happy_number(n):
    
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1
    
    
n = int(input())
res = is_happy_number(n)
if(res == True):
    ans = 1
else:
    ans = 0
print(ans)
