n = int(input())
arr = map(int, input().split())

arr = list(arr)
arr.sort(reverse=True)

print(arr[-1])
