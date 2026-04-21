# %%
def jump(nums):
    min_jump_steps = [0] * len(nums)
    for i in range(len(nums)-2, -1, -1):
        if nums[i] != 0:
            current_max_step = nums[i]
            dist_to_goal = len(nums) - 1 - i
            
            min_step = 0
            
            if current_max_step < dist_to_goal:
                min_step = float('inf')
                for j in range(1, nums[i]+1):
                    if min_jump_steps[i+j] != 0:
                        min_step = min(min_jump_steps[i+j], min_step)
                
            min_jump_steps[i] = 1 + min_step
    return min_jump_steps[0]