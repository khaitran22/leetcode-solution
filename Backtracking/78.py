def subsets(nums):
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


subsets([1, 2, 3])
