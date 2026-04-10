def threeSum(nums):
    indices = set()

    nums = sorted(nums)
    first = 0
    second = 1
    third = len(nums) - 1
    for first in range(len(nums)-1):
        second = first + 1
        if nums[first] != nums[second]:
            while second < third:
                if nums[second] + nums[third] > -nums[first]:
                    third -= 1
                elif nums[second] + nums[third] < -nums[first]:
                    second += 1
                else:
                    current_result = (nums[first], nums[second], nums[third])
                    if current_result not in indices:
                        indices.add(current_result)
                    second += 1
                    third -= 1
        third = len(nums) - 1
    
    return [list(rs) for rs in indices]

nums = [-2,0,1,1,2]
print(threeSum(nums))