# %%
import random


def threeSumClosest(nums, target) -> int:
    """
        Brute-force implementation
    """
    difference = 1e+10
    best_sum = None
    result = None
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                curr_sum = nums[i]+nums[j]+nums[k]
                curr_diff = target - curr_sum
                if abs(curr_diff) < difference:
                    difference = abs(curr_diff)
                    best_sum = curr_sum
    return best_sum

def threeSumClosest_next(nums, target):
    # O(nlogn)
    nums = sorted(nums)
    difference = 1e+10
    best_sum = nums[0]+nums[1]+nums[2]
    for i in range(len(nums)-2):
        j = i + 1
        k = len(nums) - 1
        curr_sum = nums[i]+nums[j]+nums[k]
        while j < k:
            if abs(target - curr_sum) < abs(target - best_sum):
                best_sum = curr_sum
                difference = abs(target - curr_sum)
    return best_sum


# nums = [random.randint(-10, 10) for _ in range(7)]
# target = random.randint(0, 5)
nums = [10,20,30,40,50,60,70,80,90]
target = 1
print(threeSumClosest(nums, target))
print(threeSumClosest_next(nums, target))
# print(threeSumClosest_next(nums, target) == threeSumClosest(nums, target))
# %%
