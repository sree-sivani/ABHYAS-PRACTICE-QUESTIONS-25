n = int(input())
arr = map(int, input().split())

arr = list(arr)
arr.sort(reverse=True)

runner_up_score = None
for score in arr:
    if score < max(arr):
        runner_up_score = score
        break

print(runner_up_score)
