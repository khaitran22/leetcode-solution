# %%
def maxSubArray(nums) -> int:
    if len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        max_sub = max(nums[0], 0) + nums[1]
        return max_sub
    
    left = nums[0]
    mid = nums[1]
    right = left + mid
    max_sub = max(left, max(mid, right))
    for i in range(2, len(nums)):
        temp_right = max(mid + nums[i], right + nums[i])
        left = max_sub
        mid = nums[i]
        right = temp_right
        max_sub = max(left, max(mid, right))

    return max_sub

nums = [5,4,-1,7,8]
maxSubArray(nums)
# %%
