def moveZeroes(nums):
    # if len(nums) > 1:
    #     all_zeros = True
    #     all_non_zeros = True
    #     for num in nums:
    #         if num == 0:
    #             all_non_zeros = False

    #         if num != 0:
    #             all_zeros = False

    #     if not all_non_zeros and not all_zeros:
    #         p1 = 0
    #         p2 = p1
    #         while p1 < len(nums) - 1 and p2 < len(nums) - 1:
    #             if nums[p1] != 0:
    #                 p1 += 1
    #             else:
    #                 p2 = p1 + 1
    #                 if nums[p2] == 0:
    #                     while nums[p2] == 0:
    #                         if p2 >= len(nums) - 1:
    #                             break
    #                         p2 += 1
    #                     if nums[p2] != 0:
    #                         nums[p1], nums[p2] = nums[p2], nums[p1]
    #                         p1 += 1
    #                 else:
    #                     nums[p1], nums[p2] = nums[p2], nums[p1]
    #                     p1 += 1
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[right], nums[left] = nums[left], nums[right]
            left += 1

    return nums


# nums = [73348, 66106, -85359, 53996, 18849, -
#         6590, -53381, -86613, -41065, 83457, 0]
# nums = [0, 1, 0, 3, 5]
# nums = [0, 0, 0, 2, 0, 0, 5, 8]
# nums = [1, 2, 3, 1]
nums = [0, 0, 0]
moveZeroes(nums)
print(nums)
