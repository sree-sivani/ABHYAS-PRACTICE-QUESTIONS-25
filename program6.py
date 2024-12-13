num = int(input())

arr = [0]

for i in range (1, num+1):
    if(num % i == 0):
        arr.append(i)
        


print(arr[-1])
