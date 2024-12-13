num = int(input())

arr = []

for i in range (1, num+1):
    if(num % i == 0):
        arr.append(i)
        

print(arr[0])
