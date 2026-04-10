# %%
def subsetXORSum(nums):
    def subset(nums):
        if len(nums) == 0:
            return [nums]

        result = [[]]
        for i in range(len(nums)):
            temp = []
            for r in result:
                new_r = r + [nums[i]]
                temp.append(new_r)
            result.extend(temp)
        return result

    all_subsets = subset(nums)
    xor_sum = 0
    for sub in all_subsets:
        if len(sub) == 0:
            continue
        elif len(sub) == 1:
            xor_sum += sub[0]
        else:
            temp_xor_sum = 0
            for e in sub:
                temp_xor_sum ^= e
            xor_sum += temp_xor_sum
    return xor_sum
