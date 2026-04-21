# %%
# def countArrangement(n: int) -> int:
#     """
#         Brute-force approach
#     """
#     def permute(nums):
#         result = [[]]
#         for num in nums:
#             new_result = []
#             for perm in result:
#                 for i in range(len(perm) + 1):
#                     new_result.append(perm[:i] + [num] + perm[i:])
#             result = new_result
#         return result
    
#     def is_beautiful_arrangment(perm):
#         for i, e in enumerate(perm):
#             if e % (i+1) != 0 and (i+1) % e != 0:
#                 return False
#         return True

#     nums = list(range(1, n+1))
#     all_perms = permute(nums)
#     beautiful_arrangements = 0

#     for perm in all_perms:
#         if is_beautiful_arrangment(perm):
#             # if perm[-1] == n:
#             print(perm)
#             beautiful_arrangements += 1
        
#     return beautiful_arrangements

class Solution:
    def __init__(self):  
        self.res = 0
    
    def countArrangement(self, n: int) -> int:
        
        self.res = 0
        nums = [i for i in range(1, n+1)]
        
        def dfs(nums: list, i: int = 1):
            if len(nums) == 4:
                a = 1
            if i == n+1: 
                self.res += 1
                return
            
            for j, num in enumerate(nums):
                if not(num % i and i % num):
                    dfs(nums[:j] + nums[j+1:], i+1)
            
        dfs(nums)
        return self.res

sol = Solution()
sol.countArrangement(n=4)
# %%
def permute(nums):
    result = [[]]
    for num in nums:
        new_result = []
        for perm in result:
            for i in range(len(perm) + 1):
                new_lst = perm[:i] + [num] + perm[i:]
                if num % i:
                    is_beauty_arrangment = True
                new_result.append()
        result = new_result
    return result

n = 3
permute(list(range(1, n+1)))
# %%
