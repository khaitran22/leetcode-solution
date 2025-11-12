# def twoSum(nums, target: int):
#     for i in range(len(nums)-1):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]

# def twoSum(nums, target):
#     # idx_nums = {v: k for k, v in enumerate(nums)}
#     idx_nums = {}
#     for k, v in enumerate(nums):
#         if idx_nums.get(v) == None:
#             idx_nums[v] = [k]
#         else:
#             idx_nums[v].append(k)
#     nums = sorted(nums)
#     left_idx = 0
#     right_idx = len(nums) - 1
#     while left_idx < right_idx:
#         if nums[left_idx] + nums[right_idx] < target:
#             left_idx += 1
#         elif nums[left_idx] + nums[right_idx] > target:
#             right_idx -= 1
#         else:
#             if nums[left_idx] == nums[right_idx]:
#                 return idx_nums[nums[left_idx]][:2]
#             return [idx_nums[nums[left_idx]][0], idx_nums[nums[right_idx]][0]]

def twoSum(nums, target):
    # idx_nums = {}
    # for k, v in enumerate(nums):
    #     if idx_nums.get(v) == None:
    #         idx_nums[v] = [k]
    #     else:
    #         idx_nums[v].append(k)
    
    # for num in nums:
    #     if idx_nums.get((target - num)) != None:
    #         if target == num*2 and len(idx_nums[num]) > 1:
    #             return idx_nums[num][:2]
            
    #         if target != num*2:
    #             return [idx_nums[num][0], idx_nums[(target - num)][0]] 
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[nums[i]] = i
    # Return an empty list if no solution is found
    return []

nums = [2,5,5,11]
target = 10
print(twoSum(nums, target))