# %%
def coinChange(coins, amount) -> int:
    if amount == 0:
        return 0
    coins_need = [0] * (amount + 1)
    for i in range(1, amount + 1):
        min_coin = float("inf")
        for c in coins:
            if c <= i and min_coin > (1 + coins_need[i-c]) and coins_need[i-c] > -1:
                min_coin = (1 + coins_need[i-c])
        coins_need[i] = min_coin if min_coin != float("inf") else -1
    
    return -1 if coins_need[amount] == 0 else coins_need[amount]

coinChange([1,2,5], amount=11)
# coinChange([2], amount=3)
# coinChange([1], amount=0)
# coinChange([1,4,5,10], amount=7)
# coinChange([2,5,7,8,4], amount=30)
# coinChange([37,233,253,483], amount=7163)
# %%
