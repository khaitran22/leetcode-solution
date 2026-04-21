# %%
def climbStairs(n: int):
    if n == 1:
        return 1
    prev_1_step = 1
    prev_2_step = 1
    climbing_ways = 0
    for i in range(1, n):
        climbing_ways = prev_1_step + prev_2_step
        prev_2_step = prev_1_step
        prev_1_step = climbing_ways
    return climbing_ways
n = 3
climbStairs(n)
# %%
