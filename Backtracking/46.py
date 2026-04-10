"""
    Sample solution
"""


def permute(nums):
    def backtrack(nums, candidate, used, res):
        if len(candidate) == len(nums):
            res.append(candidate[:])
            return

        for num in nums:
            if num not in used:
                candidate.append(num)
                used.add(num)

                backtrack(nums, candidate, used, res)

                candidate.pop()
                used.remove(num)
    res = []
    backtrack(nums, [], set(), res)
    return res


nums = [1, 2, 3]
print(permute(nums))
# print(4 ^ 6)

"""
    Two pointers approach:
"""
# def permute(nums):
#     def nextPermutation(nums):
#         # normal array
#         for i in range(len(nums)-1, 0, -1):
#             if nums[i-1] < nums[i]:
#                 idx_pivot = i-1
#                 rightmost_idx = i
#                 for j in range(i+1, len(nums), 1):
#                     if nums[j] > nums[idx_pivot]:
#                         rightmost_idx = rightmost_idx if nums[j] > nums[rightmost_idx] else j
#                 nums[idx_pivot], nums[rightmost_idx] = nums[rightmost_idx], nums[idx_pivot]
#                 for k in range(0, (len(nums)-i)//2, 1):
#                     nums[i+k], nums[len(nums)-1-k] = nums[len(nums)-1-k], nums[i+k]

#         return nums
#     nums = sorted(nums)
#     possible_permutation = 1
#     for i in range(len(nums)):
#         possible_permutation *= (i+1)
#     count = 1
#     result = [nums]
#     input = [i for i in nums]
#     while count < possible_permutation:
#         output = nextPermutation(input)
#         result.append(output)
#         input = [i for i in output]
#         count += 1
#     return result

# nums = [1,2,3]
# print(permute(nums))
