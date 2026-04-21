# %%
def canJump(nums) -> bool:
    goal = len(nums) - 1
    current_reach = True
    last_idx_reachable = goal
    for i in reversed(range(len(nums)-1)):
        if nums[i] >= 1:
            if i+nums[i] >= goal or i+nums[i] >= last_idx_reachable:
                last_idx_reachable = i
                current_reach = True
        else:
            current_reach = False
    return current_reach
        


# nums = [3,2,1,0,4]
# nums = [4, 4, 0, 1, 5, 5, 2, 0, 1, 1, 0, 5, 3, 5, 2]
# nums = [1, 5, 1, 3, 5, 3, 1, 3, 2, 5, 2, 1, 5, 1, 4]
# nums = [2,3,1,1,4]
# canJump(nums)

# # %%
# import random
# rand_list = [random.randint(0,5) for i in range(15)]
# rand_list
# %%
