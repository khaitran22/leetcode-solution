def nextPermutation(nums):
    # increasing arrays
    descending_only = True
    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            descending_only = False
    if descending_only:
        for i in range(0, len(nums)//2, 1):
            nums[i], nums[len(nums)-1-i] = nums[len(nums)-1-i], nums[i]
    else:
        # normal array
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                idx_pivot = i-1
                rightmost_idx = i
                for j in range(i+1, len(nums), 1):
                    if nums[j] > nums[idx_pivot]:
                        rightmost_idx = rightmost_idx if nums[j] > nums[rightmost_idx] else j
                nums[idx_pivot], nums[rightmost_idx] = nums[rightmost_idx], nums[idx_pivot]
                for k in range(0, (len(nums)-i)//2, 1):
                    nums[i+k], nums[len(nums)-1-k] = nums[len(nums)-1-k], nums[i+k]
                break

nums = [1,2,3,4]
nextPermutation(nums)
print(nums)