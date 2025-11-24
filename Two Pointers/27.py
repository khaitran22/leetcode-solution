def removeElement(nums, val):
    left = 0  # <- index for new array
    freq = 0
    for right in range(len(nums)):  # <- loop over the current array
        if nums[right] != val:
            nums[left], nums[right] = nums[right], nums[left]
            # nums[right] = "_"
            left += 1
        else:
            freq += 1
    for i in range(len(nums)-1, len(nums)-1-freq, -1):
        nums.pop(i)


# nums = [3, 2, 2, 3]
# val = 3
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
removeElement(nums, val)
print(nums)
