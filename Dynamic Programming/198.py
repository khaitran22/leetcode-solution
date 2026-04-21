# %%
def rob_bf(nums):
    """
        Brute-force Approach
    """
    def generate_binary_lists(n):
        result = [[0], [1]]
        for _ in range(1, n):
            new_result = []
            for lst in result:
                if lst[-1] == 1:
                    new_result.append(lst + [0])
                else:
                    new_result.append(lst + [1])
                    new_result.append(lst + [0])
            result = new_result
        return result
    
    all_binary_lists = generate_binary_lists(len(nums))
    max_money = float("-inf")
    current_max_robbed_house = None
    for lst in all_binary_lists:
        current_money = 0
        for i in range(len(lst)):
            current_money += lst[i] * nums[i]
            if current_money > max_money:
                max_money = current_money
    return max_money, current_max_robbed_house

def rob(nums):
    rob_amount = 0
    not_rob_amount = 0
    for i in range(len(nums)):
        # if rob this i-th house
        if i == 0:
            rob_amount += nums[i]
        else:
            amount_if_rob = not_rob_amount + nums[i]
            not_rob_amount = max(rob_amount, not_rob_amount)
            rob_amount = amount_if_rob
    return max(not_rob_amount, rob_amount)


# input = [2,1,1,2]
input = [183,219,57,193, 94, 233, 202]
rob(input)

# %%
