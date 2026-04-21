# %%
def rob_brt(nums):
    '''
        Brute-force approach
    '''
    def generate_binary_list(n):
        result = [[0], [1]]
        for _ in range(1, n):
            new_result = []
            for lst in result:
                new_result.append(lst + [0])
                if lst[-1] != 1:
                    new_result.append(lst + [1])
            result = new_result
        
        for i, lst in enumerate(result):
            if len(lst) > 1:
                if lst[0] * lst[-1] != 0:
                    result.pop(i)
        
        return result
    
    all_house_robbed = generate_binary_list(len(nums))
    max_house = float("-inf")
    max_comb = None
    for combination in all_house_robbed:
        current_max_amount = 0
        for i, is_rob in enumerate(combination):
            current_max_amount += (is_rob * nums[i])
        if current_max_amount > max_house:
            max_house = current_max_amount
            max_comb = combination
    print(max_comb)
    return max_house

# %%
def rob_dp(nums):
    def rob_I(nums):
        rob_amount_I = 0
        not_rob_amount_I = 0
        for i in range(len(nums)):
            if i == 0:
                rob_amount_I += nums[i]
            else:
                amount_if_rob_I = not_rob_amount_I + nums[i]
                not_rob_amount_I = max(rob_amount_I, not_rob_amount_I)
                rob_amount_I = amount_if_rob_I
        return max(rob_amount_I, not_rob_amount_I)
    rob_amount = 0
    not_rob_amount = 0
    for i in range(len(nums)):
        if i == 0:
            rob_amount += nums[i]
        elif i == len(nums) - 1:
            amount_if_rob = not_rob_amount + nums[i]
            not_rob_amount = max(rob_amount, not_rob_amount)
            # Compute the rob_amount satisfying the condition
            rob_amount = rob_I(nums[1:])
        else:
            amount_if_rob = not_rob_amount + nums[i]
            not_rob_amount = max(rob_amount, not_rob_amount)
            rob_amount = amount_if_rob
    return max(rob_amount, not_rob_amount)

rob_dp([94,40,49,65,21])
# %%
