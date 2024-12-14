def fascinating(n):
   

    if n < 100:
        return False

    s = str(n) + str(2 * n) + str(3 * n)
    if len(s) != 9:
        return False

    freq = [0] * 10
    for c in s:
        freq[int(c)] += 1

    for i in range(1, 10):
        if freq[i] != 1:
            return False

    return True
    
    
n = input()

arr = n.split()

val = int(arr[-1])

res = fascinating(val)

if(res == True):
    ans = "Fascinating"
else:
    ans = "Not Fascinating"

print(ans)
