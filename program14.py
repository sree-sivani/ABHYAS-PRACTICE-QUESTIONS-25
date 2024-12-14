def search_insert(nums, target):
   
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left
    
    
n = input()
n_arr = n.split()
n_val = int(n_arr[-1])


target = input()
target_arr = target.split()
target_val = int(target_arr[-1])


ans = search_insert(n_val, target_val)
print(ans)
