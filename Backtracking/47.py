def permuteUnique(nums):
    def backtrack(nums, candidate, used, res, existing_tuple):
        if len(candidate) == len(nums) and not existing_tuple.get(tuple(candidate)):
            res.append(candidate[:])
            existing_tuple[tuple(candidate)] = 1
            return

        for i, num in enumerate(nums):
            if not used[i]:
                candidate.append(num)
                used[i] = True

                backtrack(nums, candidate, used, res, existing_tuple)

                candidate.pop()
                used[i] = False

    res = []
    used = {i: False for i in range(len(nums))}
    existing_tuple = {}
    backtrack(nums, [], used, res, existing_tuple)
    return res


print(permuteUnique([1, 2, 3]))
