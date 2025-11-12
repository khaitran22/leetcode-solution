def removeDuplicates(nums):
    slow_idx = fast_idx = 0
    while fast_idx < len(nums):
        
        if nums[slow_idx] == nums[fast_idx]:
            fast_idx += 1
            continue

        if slow_idx == fast_idx - 1:
            fast_idx += 1
            slow_idx += 1
            continue
        
        slow_idx += 1
        nums[slow_idx] = nums[fast_idx]
        nums[fast_idx] = "_"
        fast_idx += 1
    count = slow_idx + 1
    slow_idx += 1
    while slow_idx < len(nums):
        nums[slow_idx] = "_"
        slow_idx += 1
    
    return count


# nums = [0,0,1,1,1,2,2,3,3,4]
nums = [0,0,0,0,0,0,0,0,0,0]
count, nums = removeDuplicates(nums)
print(count)
print(nums)